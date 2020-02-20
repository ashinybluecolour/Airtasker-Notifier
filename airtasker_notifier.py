#! /usr/bin/env python3

import requests
import os
import json

def help():
 print("usage: ./airtasker_notifier.py --lat <latitude> --lon <longitude> <job keyword>")
 print("optional arguments: --distance <maximum distance from location in km>")
 print("                    --min <minimum pay (must be >= 5)>")
 print("                    --max <maximum pay> (must be <= 9999)")
 print("                    --type <\'remote\', \'onsite\' or \'both\'>")
 print("                    --keywords <keyword 1> <keyword 2> ...")
 print("                    --no_keywords")
 os.sys.exit(0)

if (len(os.sys.argv) < 2):
 help()
 os.sys.exit(0)

lat = ""
lon = ""
distance = str(50)
min_price = str(5)
max_price = str(9999)
type = "remote"
keywords = []
check_keywords = 1

for i in range(1, len(os.sys.argv)):
 arg = os.sys.argv[i]
 if (arg == "-h"):
  help()
  os.sys.exit(0)
 elif (arg == "--no_keywords"):
  check_keywords = 0
 elif (arg == "--lat"):
  lat = "&lat="+os.sys.argv[i+1]
 elif (arg == "--lon"):
  lon == "&lon="+os.sys.argv[i+1]
 elif (arg == "--min"):
  min_price = os.sys.argv[i+1]
 elif (arg == "--max"):
  max_price = os.sys.argv[i+1]
 elif (arg == "--distance"):
  distance = str(int(os.sys.argv[i+1])*1000)
 elif (arg == "--type"):
  if (os.sys.argv[i+1] == "remote"):
   type = "remote"
  if (os.sys.argv[i+1] == "onsite"):
   type = "physical"
  if (os.sys.argv[i+1] == "both"):
   type = "both"
 elif (arg == "--keywords"):
   for j in range(1, len(os.sys.argv)-i):
    if ("--" not in os.sys.argv[i+j]):
     keywords.append(os.sys.argv[i+j])
    else:
     break

if (len(keywords) == 0 and check_keywords):
 print("Please specify keywords using --keywords, type -h for help.")
 os.sys.exit(0)

if ((type == "both" or type == "onsite") and not (lat == "lat=" or lon == "lon=")):
 print ("Please specify a latitude and longitude using --lat and --lon, type -h for help.")
 os.sys.exit(0)

req_headers = {'sort_by':'recent', 'task_states':'posted', 'task_types':'physical', 'lat':'-31.9039', 'lon':'116.2024', 'radius':'50000'}

url = 'https://www.airtasker.com/api/v2/tasks?limit=8&show_multi=true&badges=&task_states=posted'+lat+'&'+lon+'&task_types='+type+'&sort_by=recent&radius='+distance+'&max_price='+max_price+'&min_price='+min_price+'&path=tasks&threaded_comments=true'

job_words = []

for i in range(1, len(os.sys.argv)):
 job_words.append(os.sys.argv[i].lower())

jobs = []

job_name = ""

while (True):
 page = requests.get(url, headers=req_headers)

 json_data = json.loads(page.text)
     
 for job in json_data["tasks"]:
  job_name = job["name"].lower()
        
  if (check_keywords):                     
   for word in job_words:
    if (word in job_name):
     if (job_name not in jobs):
      jobs.append(job_name)
      print(job_name)
      os.system("osascript -e \'display notification \""+job_name+"\" with title \"Airtasker Job\"'")
      os.system("sleep 5")
  else:
   if (job_name not in jobs):
    jobs.append(job_name)
    print(job_name)
    os.system("osascript -e \'display notification \""+job_name+"\" with title \"Airtasker Job\"'")
    os.system("sleep 5") 
 os.system("sleep 10")
