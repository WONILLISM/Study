import csv
import requests
from bs4 import BeautifulSoup

url = "https://programmers.co.kr/learn/challenges?tab=all_challenges"
def get_max_page():
    req = requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
    pages = soup.find_all("li",{"class":"page-item"})
    max_page = pages[-2].string
    return max_page

def get_problems(num):
    page_url = f"{url}&page={num}"
    req = requests.get(page_url)
    soup = BeautifulSoup(req.text,"html.parser")
    algorithm_list = soup.find("div",{"class":"algorithm-list"}).find_all("div",{"class":"col-item"})

    # title, link, level, langs [] 
    ret = []

    for item in algorithm_list:
        tmp = {}
        tmp["title"] = item.find("h4",{"class":"title"}).string
        link = "https://programmers.co.kr"
        link += item.find("a")["href"]
        tmp["link"] = link
        tmp["level"] = item.find("div",{"class":"card-algorithm"})["class"][1]
        ret.append(tmp)

        #languages = algorithm_list[4].find("div",{"class":"languages"}).find_all("div",{"data-container":"body"})
        # langs = []
        # for language in languages:
        #     lang = language["data-original-title"]
        
    return ret
    
        
        

def process():
    max_page = int(get_max_page())

    file = open("problems.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title","link","level"])
    for i in range(1,max_page+1):
        tmp = get_problems(i)
        for j in tmp:
            writer.writerow(list(j.values()))

    return

process()
