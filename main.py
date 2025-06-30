import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wanted_job = input("search for your job: ")
wanted_location = input("Enter location that you want: ")

driver = webdriver.Firefox()

driver.get(f"https://www.linkedin.com/jobs/search?keywords={wanted_job}&location={wanted_location}&position=1&pagenum=0")

time.sleep(5)

forum = driver.find_element(By.CLASS_NAME, 'jobs-search__results-list')
jobs_listed = forum.find_elements(By.TAG_NAME, 'li')

for li in jobs_listed:
    title = li.find_element(By.CLASS_NAME, 'base-search-card__title').text
    link = li.find_element(By.TAG_NAME, 'a').get_attribute("href")
    location = li.find_element(By.CLASS_NAME , 'job-search-card__location').text
    listed_time = li.find_element(By.CLASS_NAME, "job-search-card__listdate").text

    print(f"Title: {title}, LOCATION: {location}\n, TIME:{listed_time}  , link: {link}\n")
