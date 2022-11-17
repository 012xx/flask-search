from flask import render_template, request, redirect, url_for, send_from_directory
from csv import reader
from main import app
import pandas as pd

@app.route('/',methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('search.html')
  elif request.method == 'POST':
    poststr = request.form.get("searchWord")
    return render_template('search.html', poststr = poststr)

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')

## TODO: 教授の詳細URL飛ぶとか

