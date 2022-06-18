from flask import Flask

"""
https://flask.palletsprojects.com/en/2.1.x/quickstart/

Initializing the Flask app. I was unable to get it to work with a different name
than app.py. FLASK_ENV = "name" wasn't working, so I used a shortcut by renaming 
it to app.py. 

"""

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, Y'all!</p"