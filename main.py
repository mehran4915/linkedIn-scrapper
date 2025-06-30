from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class JobScraper:
    def __init__(self, job_title, location):
        self.job_title = job_title
        self.location = location
        self.jobs_data = []

        options = Options()
        options.headless = True 
        self.driver = webdriver.Firefox(options=options)

    def scrape_jobs(self):
        self.driver.get(f"https://www.linkedin.com/jobs/search?keywords={self.job_title}&location={self.location}&position=1&pagenum=0")

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'jobs-search__results-list')))
        
        try:
            forum = self.driver.find_element(By.CLASS_NAME, 'jobs-search__results-list')
            jobs_listed = forum.find_elements(By.TAG_NAME, 'li')

            for li in jobs_listed[:3]:
                try:
                    title = li.find_element(By.CLASS_NAME, 'base-search-card__title').text
                    location = li.find_element(By.CLASS_NAME, 'job-search-card__location').text
                    listed_time = li.find_element(By.CLASS_NAME, "job-search-card__listdate").text
                    link = li.find_element(By.TAG_NAME, 'a').get_attribute("href")

                    self.jobs_data.append({
                        'Title': title,
                        'Location': location,
                        'Listed Time': listed_time,
                        'Link': link
                    })

                except Exception as e:
                    print(f"Error extracting job details: {e}")

        except Exception as e:
            print(f"Error loading job listings: {e}")

        finally:
            self.driver.quit()

