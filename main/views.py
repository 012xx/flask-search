from flask import render_template, request, redirect, url_for, send_from_directory
from csv import reader
from main import app
import pandas as pd

csvPath = "./data/data.csv"

# open file
# with open(csvPath,"r") as searchTarget:
#   # pass the file object reader()
#   reader = reader(searchTarget)
#   # do this for all the rows
#   for i in reader:
#     # print the rows
#     print(i)

@app.route("/",methods=['GET', 'POST'])
def index():
  # CSVファイルをPandasでロード
  df = pd.read_csv(csvPath)

  # データフレームをリストに変換してテンプレートに渡す
  return render_template('index.html',title="これはタイトルです",data_lists=df.values.tolist())

# def create_table():


# debug code
if __name__=='views':
    app.run(debug=True)



