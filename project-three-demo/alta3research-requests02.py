#!/usr/bin/env python3

# imports tools
import requests
import importlib  
import pprint
import json 
from flask import jsonify

# imports the flask file 
flask_app = importlib.import_module("alta3research-flask01")

# the port our app runs on 
URL= "http://127.0.0.1:2225/"

def formatting():
    #sends a get request to the home page of the app
    best_pokes = requests.get(URL).json()
    
    #prints out the best pokemon after looping through it
    for pm in best_pokes[0]["best"]:
        print("Look, Ma! It's a... \n" + pm)
#invokes function
formatting()

def poke_types():
    type_api = "https://pokeapi.co/api/v2/type/"
    # sends a get request to the pokemon API
    type_info = requests.get(type_api).json()
    print("Some pokemon types:")
    #loops through and prints the pokemon types
    for poke_type in type_info["results"]:
        pprint.pprint(poke_type["name"])
#invokes function 
poke_types()

# command for GET requests:
#curl http://0.0.0.0:2225/moves -L
