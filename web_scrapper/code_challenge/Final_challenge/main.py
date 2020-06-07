"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from flask import Flask, render_template, request, redirect
from src.scrapper import results_jobs

app = Flask("Remote Jobs")


@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search",methods=['GET','POST'])
def search():

  job_name = str(request.form['job_name']).lower()
  jobs = results_jobs(job_name)
  return render_template("search.html",jobs=jobs,job_name=job_name,num_of_jobs=len(jobs))

app.run(host="0.0.0.0")

