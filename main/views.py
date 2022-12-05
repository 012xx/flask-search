from flask import render_template, request, redirect, url_for, send_from_directory
from csv import reader
from main import app
import pandas as pd

@app.route('/',methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('search.html')
  elif request.method == 'POST':
    searchWord = request.form.get("searchWord")
    return render_template('search.html', searchWord = searchWord)
    # with open("./data/data.csv","r") as CSVfile:
      # reader = reader(CSVfile)
      # result = []
      # for row in reader:
      #   if poststr is row:
      #     result.append(row)
      #     return render_template('search.html', result = result)


if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')

## TODO: 教授の詳細URL飛ぶとか
## 1/31まで
## わからないならわからないでOK 最低限でいいので、説明書をしっかりとかく
