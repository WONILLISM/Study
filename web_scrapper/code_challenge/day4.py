import requests
import os
from bs4 import BeautifulSoup

def check_URLs(urls):
  for url in urls:
    if "." not in url:
      print(f"{url} is not a valid URL.")
    else :
      if "https://" not in url and "http://" not in url:
        url = "https://" + url
      try:
        res = requests.get(f"{url}")
        if "200" in res.status_code : print(f"{url} is up!")
        else:  print(f"{url} is down!")
      except Exception:
        print(f"{url} is down!")
      

def process():
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs to check. (separated by comma)")

  URLs = input().replace(" ","").split(",")
# print(URLs)
  check_URLs(URLs)

  while 1:
    print("Do you want to start over? y/n")
    a = input()
    if a == 'n': 
      "k. bye :)"
      break
    elif a == 'y': 
      os.system("clear")
      process()
      break
    else: 
      print("That's not a valid answer.")
  return   
    

process()