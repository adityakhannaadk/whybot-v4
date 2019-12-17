from flask import Flask
from threading import Thread
import flask
app = Flask('')

@app.route('/')
def home():
  return "Server status: up"
def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()