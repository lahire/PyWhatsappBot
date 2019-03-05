#!/usr/bin/python3

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hola Mundo!!"

@app.route("/incoming", methods=["POST"])
def incomming():
  print('Hola')
  print(dir(request))
  print(request.url)
  return 'Hola Wassap'


if __name__ == "__main__":
  app.run()
