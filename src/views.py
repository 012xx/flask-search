from src import app
from csv import reader

csvPath = "./data/data.csv"

# open file
with open(csvPath,"r") as searchTarget:
  # pass the file object reader()
  file_reader = reader(searchTarget)
  # do this for all the rows
  for i in file_reader:
    # print the rows
    print(i)

@app.route("/")
def index():
  return "Hello Flask"



