#/usr/bin/env python3
"""uses flask, jinja; creates different endpoints for API calls"""

from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import json
app = Flask(__name__)

#url = "https://pokeapi.co/api/v2/pokemon/?limit=100"
#poke_resp = app.get(url)
#print(type(poke_resp))

thelist = [{"home": "boston"}]

@app.route('/')
#removed methods = get 
def greeting(thelist):
   # with app.app_context():
   # poke_resp = app.get(url).json()
       # print(request.args['poke_resp'])
       # poke_resp = request.args['poke_resp']
   # jsonify(thelist)
    print(type(thelist))
    info = json.dumps(thelist)
    return render_template("welcome.html", data = info)
    #removed jsonify(pr) 
    #return ("Welcome to your childhood dreams:\nA website dedicated to Pokemon!\nSome pokemon:" + poke_resp["results"][0])
#@app.route("/discover")
#def discover():
   # return jsonify(poke_resp)
#    print ("discover:")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2225)
