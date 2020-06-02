import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"
brand_urls = []

def extract_brand(brand_info):
    url = brand_info["href"]
    title = brand_info.find("span",{"class":"company"}).string
    return {
        "url" : url,
        "title" : title
    }
def get_company_lists():
    request = requests.get(alba_url)
    soup = BeautifulSoup(request.text, "html.parser")
    lists = soup.find("div",{"id":"MainSuperBrand"}).find("ul",{"class":"goodsBox"})
    brands = lists.find_all("a",{"class":"goodsBox-info"})

    lists =[]
    for brand in brands:
        lists.append(extract_brand(brand))
    return lists
      
def save_to_file(l):
    try:
        request = requests.get(l["url"])
        soup = BeautifulSoup(request.text,"html.parser")
        brand_list = soup.find("div",{"id":"NormalInfo"}).find("tbody").find_all("tr",{"class":""})

        file = open(f"{l['title']}.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow(["place","title","time","pay","date"])
        
        for info in brand_list:
            place = info.find("td",{"class":"first"}).get_text()
            title = info.find("span",{"class":"company"}).get_text()
            time = info.find("span",{"class":"time"}).get_text()
            pay = info.find("td",{"class":"pay"}).get_text()
            date = info.find("td",{"class":"last"}).get_text()
            writer.writerow([place,title,time,pay,date])
    except:
        print("")
    

def main():
  lists = get_company_lists()
  for l in lists:
    save_to_file(l)


main()
