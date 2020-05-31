import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""
iban_url = "https://www.iban.com/currency-codes"
transferwize_url = "https://transferwise.com/gb/currency-converter"


def get_table():
  countries = []

  request = requests.get(iban_url)
  soup = BeautifulSoup(request.text, "html.parser")

  table = soup.find("table")
  rows = table.find_all("tr")[1:]

  for row in rows:
    items = row.find_all("td")
    name = items[0].text
    code =items[2].text
    if name and code:
      if name != "No universal currency":
        country = {
          'name':name.capitalize(),
          'code': code
        }
        countries.append(country)
  return countries

def ask(countries, i):
  try:
    cmd = [0,0]
    if i==0: cmd[i] = int(input("Where are you from? Choose a country by number.\n\n#: "))

    elif i==1: cmd[i] = int(input("Now choose another country.\n\n#: "))  

    if cmd[i] > len(countries):
        print("Choose a number from the list.")
        ask(countries, i)
    else:
      country = countries[cmd[i]]
      return country
  except ValueError:
    print("That wasn't a number.")
    ask(countries, i)

def convert(country1, country2):
  try:
    money = input(f"How many {country1['code']} do you want to convert to {country2['code']}?\n")
  except ValueError:
    print("That wasn't a number.")
    convert(country1, country2)

  request = requests.get(f"{transferwize_url}/{country1['code']}-to-{country2['code']}-rate?amount={money}")
  soup = BeautifulSoup(request.text, "html.parser")
  from_amount = soup.find("input",{"id":"cc-amount-from"})["value"]
  to_amount = soup.find("input",{"id":"cc-amount-to"})["value"]
  
  res_from =format_currency(from_amount,country1['code'], locale="ko_KR")
  res_to = format_currency(to_amount,country2['code'],locale="ko_KR")
  print(f"{res_from} is {res_to}")
  
  
def main():
  print("Welcome to CurrencyConvert PRO 2000\n")
  countries = get_table()
  for index, country in enumerate(countries):
    print(f"#{index} {country['name']}")

  country1 = ask(countries,0)
  print(f"{country1['name']}\n")
  country2 = ask(countries,1)
  print(f"{country2['name']}\n")
  
  # country1 = countries[50]
  # country2 = countries[126]
  convert(country1,country2)
    
  return

main()