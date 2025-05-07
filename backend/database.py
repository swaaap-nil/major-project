import json
import psycopg2
from tabulate import tabulate
from config import DB_CONFIG

conn = psycopg2.connect(**DB_CONFIG)
# def dropTable():
#     try:
#         # Create a cursor object to interact with the database
#         cursor = conn.cursor()

#         # Query to drop the table
#         drop_query = """
#         DROP TABLE IF EXISTS skills;
#         """
        
#         cursor.execute(drop_query)
#         conn.commit()
#         print("Table 'job_data' has been dropped successfully.")

#     except Exception as e:
#         print("Error dropping table:", e)

#     finally:
#         # Close the cursor and connection
#         if 'cursor' in locals() and cursor is not None:
#             cursor.close()

def listTables():
    try:
        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Query to fetch data from the job_data table
        select_query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
        """
        
        cursor.execute(select_query)
        
        # Fetch all rows from the executed query
        rows = cursor.fetchall()
        print(cursor.description)
        # Fetch column names
        colnames = [desc[0] for desc in cursor.description]

        # Pretty print the data using tabulate
        print("Data from job_data table:")
        print(tabulate(rows, headers=colnames, tablefmt="grid"))

    except Exception as e:
        print("Error fetching data:", e)

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()

def printTable():
    try:
        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Query to fetch data from the job_data table
        select_query = """
        SELECT Count(*) from linkedin_data LIMIT 2
        """
        
        cursor.execute(select_query)

        # Fetch all rows from the executed query
        rows = cursor.fetchall()
        
        # Fetch column names
        colnames = [desc[0] for desc in cursor.description]
        print(colnames)
        # Pretty print the data using tabulate
        print("Data from linkedin table:")
        print(tabulate(rows, headers=colnames, tablefmt="grid"))

    except Exception as e:
        print("Error fetching data:", e)

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()

def countEntries():
    try:
        cursor = conn.cursor()

        select_query = """
        SELECT COUNT(*) from linkedin_data
        """
        cursor.execute(select_query)
        rows = cursor.fetchone()
        return str(rows[0])

    except Exception as e:
        print("Error fetching data:", e)

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()

def dayWiseData():
    try:
        cursor = conn.cursor()
        select_query = """
        SELECT DATE(create_date) AS day, COUNT(*) AS count
        FROM linkedin_data
        GROUP BY DATE(create_date)
        ORDER BY DATE(create_date) ASC;
        """
        cursor.execute(select_query)
        rows = cursor.fetchall()
        return [{ "date": str(row[0]), "count": row[1] } for row in rows]  # Convert to list of dicts
    except Exception as e:
        print(f"Error: {e}")
        return None

def companyWiseData():
    try:
        cursor = conn.cursor()
        select_query = """
        SELECT company, COUNT(*) 
        FROM linkedin_data
        GROUP BY company
        ORDER BY count DESC
        LIMIT 5;
        """
        cursor.execute(select_query)
        rows = cursor.fetchall()
        print(rows)
        return [{ "label": str(row[0]), "value": row[1] } for row in rows]  # Convert to list of dicts
    except Exception as e:
        print(f"Error: {e}")
        return None

def domainWiseData():
    try:
        cursor = conn.cursor()
        select_query = """
        SELECT DATE(create_date) AS day, COUNT(*) AS count
        FROM linkedin_data
        GROUP BY DATE(company)
        ORDER BY COUNT DESC;
        """
        cursor.execute(select_query)
        rows = cursor.fetchall()
        return [{ "date": str(row[0]), "count": row[1] } for row in rows]  # Convert to list of dicts
    except Exception as e:
        print(f"Error: {e}")
        return None

def fetchDailyStatistics():
    try:
        total_entries = countEntries()  
        daily_data = dayWiseData()  
        
        dashboard_data = {
            "total_entries": total_entries,
            "daily_data": daily_data
        }
        
        return dashboard_data  
    except Exception as e:
        print(f"Error: {e}")
        return None
