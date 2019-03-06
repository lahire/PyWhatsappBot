#!/usr/bin/python3
# WikiBOT

from flask import Flask, request, jsonify
import requests
import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.SID = os.environ.get('SID')
app.KEY = os.environ.get('KEY')
client = Client(app.SID,app.KEY)

def welcome_user(lang='es'):
  """
  Welcomes the user
  """
  WELCOME_MESSAGE = {
  'es': 'Hola! Soy un bot que consulta Wikipedia. Para usarme escribime aglo y te respondo con el artículo! 👉 ',
  'en': "Hello! i'm a bot that searchs Wikipedia. To use me, write to me something that you want to look for in Wikipedia and i shall give it to you! :D"
  }
  return WELCOME_MESSAGE[lang]

def body_process(cuerpo):
  """
  Tries to understand the body of the message. At least, 
  
  
  """

@app.route("/")
def hello():
  return "Para usar el bot:  Manda wassap a +1 415 523 8886 with code join yet-door.!"

@app.route("/incoming", methods=["POST"])
def incomming():
#  url = request.url
#  body = {'Body':'Dijiste {0}'.format(request.form['Body'])}
#  print(r.text
#  print(dir(request))
#  print(request.url)
#  print(request.form)
#  print(request.form['Body'])
  cuerpo = request.form['Body']
  resp = MessagingResponse()
  if 'ayuda' in cuerpo.lower():
    resp.message(welcome_user('es'))
  elif 'help' in cuerpo.lower():
    resp.message(welcome_user('en'))
  else:
    resp.message('Mensaje')
  return str(resp)


if __name__ == "__main__":
  app.run()
