# Scraping LinkedIn Job Descriptions

## As a job seeker, would it help to get a certification like AZ-900 Azure Fundamentals or GCP's Cloud Associate or AWS' Cloud Practitioner?

In my efforts to upskill, while actively looking for opportunities, I found that getting a certification would not only validate my expertise but also illustrate my interest in constantly learning in the dynamically changing tech landscape. However, preparing for an exam takes commitment, and I was curious to find out whether it would be worthwhile. 

## Project Scope

This project focuses on analyzing the extent of demand for certifications in four specific job titles: data analyst, data scientist, data engineer, and Python developer. LinkedIn is used to perform the job search, and two keywords (exam, certification) are used to detect the demand. 

In this repository, there are three files:
- main.py - a Python script that uses selenium to scrape job descriptions for different roles from LinkedIn
- user_credentials.txt - first line must contain email address and second line must contain password for LinkedIn login
- EDA_JobDescriptions.ipynb - jupyter notebook for exploratory data analysis

## Main.py

Selenium's WebDriver is used for automating the LinkedIn login and job search process. Google Chrome is used as the browser. The job description is extracted by using Selenium's find_element method. The script clicks through each job on a page and saves the job descriptions, up to 5 pages (total_pages variable). <br><br>
BeautifulSoup is used to strip HTML from job descriptions. <br><br>
Then, the array with job descriptions is exported into a csv file which is then used for further analyses. 
