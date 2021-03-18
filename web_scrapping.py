# Import neccessary modules
import requests
from bs4 import BeautifulSoup
import html5lib
import os
def web_scrapping():
    # Define the url of site that needs to be scrapped
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    # establish get request
    r = requests.get(url)
    # read the html content using .text
    html_content = r.text
    # use BeautifulSoup for scrapping
    soup = BeautifulSoup(html_content)
    
    
    # grabs the all jobs from website
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    # use this varialble for giving filename. if you want to print the content than it not needed
    i=0
    # name of folder in which all text file will save
    folder = "jobs"
    parent_dir = str(os.getcwd())
    path = os.path.join(parent_dir,folder)
    os.mkdir(path) 
    # iterate through each job to find the relevent information
    for job in jobs:
        # we want to find the the jobs which is published few days ago only
        days = job.find('span', class_="sim-posted").text.strip()
        if "few" in days:
            company_name = job.find('h3', class_="joblist-comp-name").text.strip()
            skills = job.find('span', class_="srp-skills").text.strip()
            details = job.find('a')['href']
            days = job.find('span', class_="sim-posted").text.strip()
            i+=1
            # visit the button for further description on site
            soup2 = BeautifulSoup(requests.get(details).text)
            desc = soup2.find('div', class_="jd-desc job-description-main").text.strip().replace("Job Requirement / Description","")
            # create .txt file with all above description
            with open(f'{path}/{i}.txt','w') as f:
                f.write(f'company: {company_name}\nskills: {skills}\ndetails: {details}\n{desc}')
                
if __name__ == "__main__":
    web_scrapping()
    
