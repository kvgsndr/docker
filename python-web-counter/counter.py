import os
from flask import Flask

app = Flask(__name__)

x = 0
_port = os.environ.get('PORT')
if not _port:
  _port = 5000

@app.route('/inc')
def ApiInc():
    global x
    x = x + 1
    return "Num: " + str(x)

@app.route('/dec')
def ApiDec():
    global x
    x = x - 1
    return "Num: " + str(x)

@app.route('/')
def ApiBase():
    return "Num: " + str(x)

app.run(host='0.0.0.0', port=_port) 