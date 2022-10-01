#!/usr/bin/python3

# imports tools
from flask import Flask
from flask import jsonify
from flask import render_template
import requests   
import json
from random import randint as ri

# creates an instance of the Flask object
app = Flask(__name__)

best_pokemon = [{
    "title": "best pokemon", 
    "best": ["Suicune", 
            "Pikachu", 
            "Mewtwo"
        ]
    }]

#targets the home endpoint
@app.route('/') 
def get_pokes():
    # returns a jsonfied version of the the best pokemon 
    return jsonify(best_pokemon)
    
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
