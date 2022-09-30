#!/usr/bin/env python3

# imports tools
import requests
import importlib  

# imports the flask file 
flask_app = importlib.import_module("alta3research-flask01")

def formatting():
    # gives us access to working with the flask app
    with flask_app.app.app_context():
        # takes the JSON from the get_pokes function and formats it
        print(flask_app.get_pokes()["name"])
#invoked function
formatting()

# commands for GET requests:
#curl http://0.0.0.0:2225/moves -L
#curl http://0.0.0.0:2225/ -L
