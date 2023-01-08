from flask import render_template, request, redirect, url_for, send_from_directory
from csv import reader
from main import app
import pandas as pd

csvPath = "./data/data.csv"

@app.route("/",methods=['GET'])
def index():
  # データを取得する
  df = pd.read_csv(csvPath)

  # queryがある場合には上のデータからqueryでfilterかけてデータを削除する
  searchWord = request.args.get('search', '')
  csv_list = df.values.tolist()

  data_list = []

  if searchWord:
    for data in csv_list:
      # もしdata要素にsearchWordがなければ、i番目の要素を削除する
      searchData = [data[0], data[3], data[4], data[5]]
      for item in searchData:
        if type(item) is str and searchWord in item:
          data_list.append(data)
          break
  else:
    data_list = csv_list

  return render_template('index.html', searchWord=searchWord, data_list=data_list)

# CSVファイルの全データを出力するpath
@app.route("/all",methods=['GET'])
def all():
  # CSVファイルをPandasでロード
  df = pd.read_csv(csvPath)

  # データフレームをリストに変換してテンプレートに渡す
  return render_template('index.html',data_lists=df.values.tolist())

# 検索するときのpath
@app.route("/search",methods=['GET', 'POST'])
def search():
  if request.method == 'GET':
    searchWord = request.form.get("searchWord")
    return render_template('search.html', searchWord = searchWord)
  elif request.method == 'POST':
    return render_template('search.html')


if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')

## TODO: 教授の詳細URL飛ぶとか
## 1/31まで
## わからないならわからないでOK 最低限でいいので、説明書をしっかりとかく
