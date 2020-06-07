"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

import requests
from bs4 import BeautifulSoup

stackoverflow_url = "https://stackoverflow.com/jobs?r=true&q="
weworkremotely_url = "https://weworkremotely.com/remote-jobs/search?term="
remoteok_url = "https://remoteok.io/remote-" #+jobs

def scrape_SO(url):
    ret = []
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        job_lists = soup.find("div",{"class":"listResults"}).find_all("div",{"class":"grid--cell fl1"})
        
        for i in job_lists:
            tmp = {}
            info = i.find("h2",{"class":"mb4"}).find("a")
            tmp['link'] = "https://stackoverflow.com"+info['href']
            tmp['title'] = info['title']
            tmp['company'] = i.find("h3",{"class":"fc-black-700"}).find("span").string.strip()
            ret.append(tmp)
            
    except:
        pass
    return ret


def scrape_WWR(url):
    ret =[]
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        job_lists = soup.find("section",{"class":"jobs"}).find_all("li",{"class":"feature"})        
        
        for i in job_lists:
            tmp = {}
            tmp['link'] = "https://weworkremotely.com"+i.find("a")['href']
            tmp['title'] = i.find("span",{"class":"title"}).string
            tmp['company'] = i.find("span",{"class":"company"}).string
            ret.append(tmp)        
    except:
        pass
    return ret


def scrape_RO(url):
    ret =[]
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        job_lists = soup.find_all("tr",{"class":"job"})
        
        for i in job_lists:
            tmp = {}
            tmp['link'] = "https://remoteok.io/"+i['data-url']
            tmp['title'] = i['data-search']
            tmp['company'] = i['data-company']
            ret.append(tmp)        
    except:
        pass
    return ret


def results_jobs(job_name):
    jobs = []
    SO_url = f"{stackoverflow_url}{job_name}"
    WWR_url = f"{weworkremotely_url}{job_name}"
    RO_url = f"{remoteok_url}{job_name}-jobs"
    
    jobs+=scrape_SO(SO_url)
    jobs+=scrape_WWR(WWR_url)
    jobs+=scrape_RO(RO_url)

    return jobs






