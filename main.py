import csv

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from bs4 import BeautifulSoup

options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get('https://www.linkedin.com/login/')

# Read user credentials
with open('user_credentials.txt', 'r', encoding='utf-8') as file:
    user_credentials = file.readlines()
    user_credentials = [line.rstrip() for line in user_credentials]

username = user_credentials[0]
password = user_credentials[1]
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
time.sleep(1)

# Execute login
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
driver.implicitly_wait(15)
print('Login successful!')

# Job search query for data analyst in Canada
# driver.get('https://www.linkedin.com/jobs/search/?keywords=data%analyst&location=Canada')
# driver.get('https://www.linkedin.com/jobs/search/?keywords=data%scientist&location=Canada')
# driver.get('https://www.linkedin.com/jobs/search/?keywords=data%engineer&location=Canada')
driver.get('https://www.linkedin.com/jobs/search/?keywords=python%developer&location=Canada')
time.sleep(1)
print('Searching for jobs')

job_descriptions = []

total_pages = 6 # Number of pages jds will be collected from
for page in range(1, total_pages):
    print('Collecting job descriptions from page ', page)
    jobs_block = driver.find_element(By.CLASS_NAME, 'jobs-search-results-list')
    jobs_list = jobs_block.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')
    for jobs in jobs_list:
        try:
            jobs.click()
            time.sleep(1)
            job_details = driver.find_element(By.TAG_NAME, 'article').text
            soup = BeautifulSoup(job_details, "html.parser")
            job_descriptions.append(soup)
        except NoSuchElementException():
            continue
    driver.find_element(By.XPATH, f"//button[@aria-label='Page {page + 1}']").click()
    time.sleep(5)
driver.quit()

print("Exporting job descriptions to csv")
# Change file name accordingly
with open('python_ddeveloper_ca.csv', 'w') as f:
    mywriter = csv.writer(f)
    for x in job_descriptions: mywriter.writerow([x])
