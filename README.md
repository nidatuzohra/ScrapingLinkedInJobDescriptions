# Scraping LinkedIn Job Descriptions

In this repository, there are two files:
- main.py - a Python script that uses selenium to scrape job descriptions for different roles from LinkedIn
- user_credentials.txt - first line must contain email address and second line must contain password for LinkedIn login

## Main.py

Selenium's WedDriver is used for automating the LinkedIn login and job search process. Google Chrome is used as the browser. The job description is extracted by using Selenium's find_element method. The script clicks through each job on a page and saves the job descriptions, up to 5 pages (total_pages variable). <br><br>
BeautifulSoup is used to strip HTML from job descriptions. <br><br>
Then, the array with job descriptions is exported into a csv file which is then used for further analyses. 
