"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
from flask import Flask, render_template, request, redirect, send_file
from src.scrapper import results_jobs, save_csv

app = Flask("Remote Jobs")


@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search",methods=['GET','POST'])
def search():
  job_name = str(request.form['job_name']).lower()
  jobs = results_jobs(job_name)
  save_csv(jobs, job_name)
  return render_template("search.html",jobs=jobs,job_name=job_name,num_of_jobs=len(jobs))
  
@app.route("/download")
def download():
  file_name = f"static/csv/jobs.csv"
  return send_file(
    file_name, mimetype='text/csv',
    attachment_filename='jobs.csv',
    as_attachment=True
  )

app.run(host="0.0.0.0",port=5002,debug=True)
