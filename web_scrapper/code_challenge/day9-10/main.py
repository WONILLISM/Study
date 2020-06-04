import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"
get_new = requests.get(new).json()['hits']
get_popular = requests.get(popular).json()['hits']
db = {}
db[new] = get_new
db[popular] = get_popular

app = Flask("DayNine")
@app.route("/")
def home():
  temp = request.args.get('order_by')
  # print(temp)
  if temp == 'new':
    return render_template("index.html", db = db[new], temp="new")
  else:
    return render_template("index.html", db = db[popular], temp="popular") 

@app.route("/<id>")
def detail(id):
  comments = requests.get(make_detail_url(id)).json()
  comments_list = comments['children']
  
  return render_template(
    "detail.html", 
    comments = comments,
    comments_list = comments_list
  )

app.run(host="0.0.0.0")