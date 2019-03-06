#!/usr/bin/python3

from flask import Flask, request, jsonify
import requests
import os


app = Flask(__name__)
app.SID = os.environ.get('SID')
app.KEY = os.environ.get('KEY')

@app.route("/")
def hello():
  return "Hola Mundo!!"

@app.route("/incoming", methods=["POST"])
def incomming():
  print('Hola')
  print(dir(request))
  print(request.url)
  print(request.form)
  print(request.form['Body'])
  return 'Hola Wassap'


if __name__ == "__main__":
  app.run()
