from flask import Flask, render_template

app = Flask(__name__)


def getNextHam():
  # Read a records from adif
  # Check if the QSO has already been saved
  
  call = 'R3UBU'
  QSODateTime = '21.01.2022 14:11:10'
  band = '20m'
  mode = 'FT8'
  RSTr = -11
  qrzCom = 'https://www.qrz.com/db/' + call
  qrzRu = 'https://www.qrz.ru/db/' + call
  
  # Class Ham to store data about an op
  
  ham = new Ham();
  
  return ham;

@app.route('/')
def displayHam():
  # on GET
  data = getNextHam()
  
  # on POST
  saveQSO()
  data = getNextHam()
  
  return render_template('index.html', ham=data)
