#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hola Mundo!!"

@app.route("/incoming")
def incomming():
  return 'Hola Wassap'


if __name__ == "__main__":
  app.run()
