import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""
base_url = "https://www.reddit.com/r"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

app = Flask("DayEleven")

@app.route("/")
def home():
  return render_template("home.html",subreddits=subreddits)

@app.route("/read")
def read():
  arg = request.args.copy()
  results = list(arg)
  db = []
  for res in results:
    lang = []
    url = f"{base_url}/{res}/top/?t=month"
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text,"html.parser")
    posts = soup.find_all("div",{"class":"Post"})
    try:
      for post in posts:
        tmp ={}
        if(post.find("span",text="promoted")):
          pass
        else:
          tmp['lang'] = res
          if post.find('a').get('href'):
            tmp['link'] = str(post.find("a")['href'])
          if post.find('h3'):
            tmp['title'] = post.find("h3").text
          if post.find("div",{"style":"color:#1A1A1B"}):
            tmp['likes'] = int(post.find("div",{"style":"color:#1A1A1B"}).text)
          lang.append(tmp)
      db = db + lang
    except:
      pass
  db = sorted(db,key=lambda x: x['likes'], reverse=True)
  return render_template("read.html",db=db,arg=arg)



app.run(host="0.0.0.0")