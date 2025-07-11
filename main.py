import csv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LinkedInJobScraper:
    def __init__(self, job_title, location):
        self.job_title = job_title
        self.location = location
        self.jobs_data = []

        options = Options()

        self.driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
        )

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

                    print(self.jobs_data)

                except Exception as e:
                    print(f"Error extracting job details: {e}")

        except Exception as e:
            print(f"Error loading job listings: {e}")

        finally:
            self.driver.quit()

    def save_to_csv(self, filename="linkedin_jobs.csv"):
            if not self.jobs_data:
                print("No job data to save.")
                return

            try:
                with open(filename, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=self.jobs_data[0].keys())
                    writer.writeheader()
                    writer.writerows(self.jobs_data)
                print(f"Data saved to {filename}")
            except Exception as e:
                print(f"Failed to save CSV: {e}")



if __name__ == "__main__":
    job_wanted = input("what job are you seeking ? : ")
    location_wanted = input("Where do you want to work ? : ")
    scraper = LinkedInJobScraper( job_wanted , location_wanted)
    scraper.scrape_jobs()
    scraper.save_to_csv(f"{job_wanted}_{location_wanted}.csv")
