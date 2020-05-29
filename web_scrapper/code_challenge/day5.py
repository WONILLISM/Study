import os
import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

def restart(Max, countries):
  cmd = input("#: ")
  
  if not cmd.isdigit():
    print("That wasn't a number.")
    restart(Max, countries)
  elif int(cmd) not in range(Max):
    print("Choose a number from the list.")
    restart(Max, countries)
  else:
    print(f"You choose {countries[int(cmd)][0]}.")
    print(f"The currency code is {countries[int(cmd)][2]}.")

  return
  

def extract_page():
  res = requests.get(url)
  soup = BeautifulSoup(res.text, "html.parser")
  table = soup.find("table",{"class":"table-bordered"})
  rows = table.find("tbody").find_all("tr")
  
  countries = {}
  idx = 0
  for row in rows:
    tmp = row.find_all("td")
    tmp = [tmp[i].string if i!=0 else tmp[i].string.capitalize() for i in range(len(tmp))]
    countries[idx] = tmp
    idx+=1

  return countries

def main():
  os.system("clear")

  print("Hello! Please choose a country by number: ")
  countries = extract_page()

  Max = len(countries)-1
  for key, value in countries.items():
    print(f"# {key} {value[0]}")
  
  restart(Max,countries)
  

main()