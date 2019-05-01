WhatsApp WikiBot
=================

A simple example on how to connect Twilio / Python and Whatsapp using flask and python magic. Neat!


Powered by Twilio WhatsApp API and Wikipedia API 🤖

# What does it use?
* Twilio for communicating with whatsapp
* Python 3 
* Flask for tiny webserviness
* phonenumbers for number prediction (gets country code of sender)

# How?
By getting a request from whatsapp, we can search on wikipedia (or another project) using the [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page) and return to the user the specific article (or an invitation to edit, if the article does not exist).

Ideally, we can capture the phone numbers country code and redirect to a specific wikipedia of said language (taking in consideration language fallbacks of mediawiki projects), to allow the user to simple type what they are looking for.


# Requires
````
pip install -r requirements.txt 
````

* Flask
* twilio
* pyyaml
* phonenumbers

9 out of 10 doctors recommend using a virtual environment for your local python use.

It is also interesing to allow Flask debug
````
export FLASK_DEBUG=1
````
to allow more verbose output.


# How to setup
After installing the requeriments, we need to create a .yaml file with our API keys. Be mindful to put this file on a secure location and on the gitignore.

````
$ cat my_config.yaml
SID: my_SID
KEY: my_API_key
````
With this file, we can run the server with
````
python3 server.py /path/to/yaml
````
By default, ````server.py```` looks for a file called ````config.yaml```` located in the same directory.

After this, the server will be running at port 5000. You can test it:

````
curl -X POST \
  http://localhost:5000/incoming \
  -d 'From=%2B5491150390381&Body=Mar%C3%ADa%20Magdalena&To=%2B14155238886'
````
That will get the Wikipedia Page for María Magdalena (using this example to show the use of tildes)

# The future
There is only war.

But really, there is a potential in reading the first numbers of a cellphone to get the country code to redirect the user to a specific wiki.

Also, metrics, and privacy.