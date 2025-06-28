import time
import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()

driver = webdriver.Firefox()

driver.get("https://www.linkedin.com")

time.sleep(10)


google_signin = driver.find_element(By.CLASS_NAME, 'google-auth-button')
google_signin.click()

windows = driver.window_handles
driver.switch_to.window(windows[-1])

Email = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
email_input = driver.find_element(By.ID, "identifierId")
email_input.send_keys(Email)

