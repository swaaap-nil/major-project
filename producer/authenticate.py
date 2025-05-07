from multiprocessing import AuthenticationError
import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from scraper.utils.chrome_driver import get_default_driver_options
from credentials import getRandomLoginCredential



def sleep_for_random_time():
    random_sleep_time = random.uniform(2, 5)
    print(f"Sleeping for {random_sleep_time:.2f} seconds...")
    sleep(random_sleep_time)
    
def get_li_at_for(credential):  
    id = credential['id']
    password = credential['password']
    
    options = get_default_driver_options(headless=False)
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd('Network.enable', {})
    driver.execute_cdp_cmd('Page.setBypassCSP', {'enabled': True})
    driver.set_page_load_timeout(15)
    try:
        driver.get("https://www.linkedin.com/login")
        sleep_for_random_time()
        user_agent = driver.execute_script("return navigator.userAgent;")
        print(f"User Agent: {user_agent}")
        username_input = driver.find_element(by=By.ID,value="username")
        username_input.send_keys(id)
        sleep_for_random_time()
        password_input = driver.find_element(by=By.ID,value="password")
        password_input.send_keys(password)
        sleep_for_random_time()

        sign_in_button = driver.find_element(by=By.XPATH, value='//button[@type="submit"]')
            
        sign_in_button.click()
        sleep_for_random_time()
        if('security' in driver.title.lower()):
            raise Exception('authentication security triggered')
        # Extract the 'li_at' cookie
        li_at_cookie = driver.get_cookie("li_at")
        if li_at_cookie:
            print(f"li_at Cookie: {li_at_cookie['value']}")
            return li_at_cookie['value']
        else:
            print("li_at Cookie not found.")
            return None
    except Exception as e:
        raise e
    finally:
        driver.quit()

if __name__=='__main__':
    print(get_li_at_for(getRandomLoginCredential()))

def generateCookie():
    credential = getRandomLoginCredential()
    print("trying to get token for",credential['id'])
    return get_li_at_for(credential)