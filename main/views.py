from flask import render_template
from csv import reader
from main import app

csvPath = "./data/data.csv"

# open file
# with open(csvPath,"r") as searchTarget:
#   # pass the file object reader()
#   reader = reader(searchTarget)
#   # do this for all the rows
#   for i in reader:
#     # print the rows
#     print(i)

@app.route("/")
def index():
  return render_template('index.html')

# debug code
if __name__=='views':
    app.run(debug=True)



