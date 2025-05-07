import ctypes
import logging
import os
import sys
from turtle import update
import psycopg2
from rabbitmq import RabbitMQHelper

from job_titles import getRandomJobTitle
from psycopg2 import OperationalError
from config import DB_CONFIG
from authenticate import generateCookie
from producer.scraper.events.events import EventData, EventMetrics, Events
from producer.scraper.exceptions.exceptions import InvalidCookieException
from producer.scraper.filters.filters import ExperienceLevelFilters
from producer.scraper.linkedin_scraper import LinkedinScraper
from producer.scraper.query.query import Query, QueryFilters, QueryOptions
logging.basicConfig(level=logging.ERROR)
from datetime import datetime
conn = None

def setupDatabase():
    global conn
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        create_linkedin_data_table = """
        CREATE TABLE IF NOT EXISTS linkedin_data (
            row_no SERIAL PRIMARY KEY,           -- Auto-incrementing unique ID for each job
            job_id VARCHAR(255) UNIQUE,          -- LinkedIn job ID for each job
            query VARCHAR(255),                  -- The query string used to find the job
            location VARCHAR(255),               -- Job location
            job_index INT,                       -- Index of the job for debugging
            link TEXT,                           -- Link to the job posting
            apply_link TEXT,                     -- Link to apply for the job
            title VARCHAR(255),                  -- Job title
            company VARCHAR(255),                -- Company name
            company_link TEXT,                   -- Link to the company profile
            company_img_link TEXT,               -- Link to the company's image/logo
            place VARCHAR(255),                  -- Place of the job
            description TEXT,                    -- Job description
            post_date VARCHAR(255),              -- Date the job was posted
            insights TEXT[],                     -- Array of insights about the job
            skills TEXT[],                       -- Array of skills required for the job
            create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Auto-set create date when the record is inserted
        );
        """

        cursor.execute("SET statement_timeout = 5000;")
        cursor.execute(create_linkedin_data_table)

        print("linkedin_data table created successfully!")

    except Exception as e:
        print("Error setting up database:", e)
        if conn:
            conn.close()
        conn = None  # Mark connection as unavailable
    finally:
        if cursor:
            cursor.close()

def ensureConnection():
    """Ensure the global database connection is alive and reconnect if necessary."""
    global conn
    try:
        if conn is None or conn.closed:
            print("Reconnecting to the database...")
            setupDatabase()
    except OperationalError as e:
        print("Database connection error:", e)
        conn = None  # Reset the connection

# Fired once for each successfully processed job
def on_data(data: EventData):
    
    new_description = data.description.replace('\n', ' ').replace('\r', ' ') # sanitized description
    updated_data = data._replace(description=new_description)
    global conn
    ensureConnection()
    if conn is None:
        print("Database connection is not available. Skipping data insertion.")
        exit()

    try:
        cursor = conn.cursor()

        # Insert data into the linkedin_data table
        insert_query = """
        INSERT INTO linkedin_data (
            job_id, query, location, job_index, link, apply_link, title, company,
            company_link, company_img_link, place, description,
            post_date, insights, skills  
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (
            data.job_id, data.query, data.location, data.job_index, data.link, data.apply_link,
            data.title, data.company, data.company_link, data.company_img_link, data.place,
            updated_data.description, data.date, data.insights, data.skills
        ))
        conn.commit()
        print('[SCRAPED]', updated_data.job_id, updated_data.title)
        rabbitmq.publish_message("notifications_queue", {
            "job_id": updated_data.job_id,
            "title": updated_data.title,
            "company":updated_data.company,
            "link": updated_data.link,
            "location": updated_data.location,
            "timestamp": datetime.now().timestamp()
        })


    except Exception as e:
        print("Error inserting data:", e)
        conn.rollback()

    finally:
        if cursor:
            cursor.close()

# Fired once for each page (25 jobs)
def on_metrics(metrics: EventMetrics):
    print('[ON_METRICS]', str(metrics))

def on_error(error):
    print('[ON_ERROR]', error)

def on_end():
    print('[ON_END]')

os.environ['LI_AT_COOKIE'] = generateCookie()

# Initialize scraper
scraper = LinkedinScraper(
    chrome_executable_path=None,
    chrome_binary_location=None,
    chrome_options=None,
    headless=True,
    max_workers=1,
    slow_mo=0.9,
    page_load_timeout=40
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

if __name__ == '__main__':
    setupDatabase()
    rabbitmq = RabbitMQHelper(host='3.111.45.66')
    print('li_at_cookie:',os.environ['LI_AT_COOKIE'])
    queries = [
        Query(
            query=getRandomJobTitle(),
            options=QueryOptions(
                locations=['India'],
                apply_link=True,
                skip_promoted_jobs=False,
                page_offset=0,
                limit=100,
                filters=QueryFilters(
                    experience=[ExperienceLevelFilters.ENTRY_LEVEL],
            )
            )
            
        ),
    ]

    try:
        scraper.run(queries)
    except KeyboardInterrupt:
        print("Shutting down scraper...")

        # Gracefully closing the database connection
        try:
            if conn:
                conn.close()
                print("Database connection closed.")
            else:
                print("No database connection to close.")
        except Exception as e:
            print("Error closing database connection:", e)

        sys.exit(0)

    except InvalidCookieException:
        print("Invalid cookie exception encountered.")
        if conn:
            conn.close()
            print("Database connection closed due to InvalidCookieException.")
        sys.exit(202)

    except Exception as e:
        # Catch any other exceptions that may occur
        print("An error occurred:", e)
        if conn:
            conn.close()
            print("Database connection closed due to an error.")
        sys.exit(1)

