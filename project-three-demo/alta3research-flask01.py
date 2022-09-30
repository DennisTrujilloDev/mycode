#!/usr/bin/python3

# imports tools
from flask import Flask
from flask import jsonify
from flask import render_template
import requests   
import json

# creates an instance of the Flask object
app = Flask(__name__)

#targets the home endpoint
@app.route('/')
def get_pokes(): 
    p_api = "http://pokeapi.co/api/v2/pokemon/?limit=100"   
    # sends a get request to the pokemon API
    info = requests.get(p_api).json()     
    #iterates over the response
    for indiv in info['results']:
        #jsonifies one of the elements 
        jsonify(indiv)
    #returns the first element, ending loop    
    return indiv 
    
#targets the /moves endpoint
@app.route('/moves')
def second():
    moves_api = "https://pokeapi.co/api/v2/move/"
    # sends a get request to the pokemon API  
    response = requests.get(moves_api).json()
    # sends data to hmtl file and returns the file
    return render_template("index.html", moves_list = response)

if __name__ == "__main__":
    #runs the app
    app.run(host="0.0.0.0", port=2225)
