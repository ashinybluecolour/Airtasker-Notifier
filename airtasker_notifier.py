#! /usr/bin/env python

import requests
import bs4
import os

if (len(os.sys.argv) < 2):
    print("Usage: ./airtasker_notifier.py <job keyword1> <job keyword2> ...")
    os.sys.exit(0)

url = 'https://airtasker.com/tasks/'

job_words = []

for i in range(1, len(os.sys.argv)):
    job_words.append(os.sys.argv[i])

    
jobs = []

while (True):
    page = requests.get(url)

    soup = bs4.BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('span', class_='new-task-list-item__title')

    for job in results:
        job = job.text.lower()

        for word in job_words:
            if (word in job):
                if (job not in jobs):
 		    jobs.append(job)
            	    print(job)
           	    os.system("osascript -e \'display notification \""+job+"\" with title \"Airtasker Job\"'")
           	    os.system("sleep 5")
    os.system("sleep 10")
