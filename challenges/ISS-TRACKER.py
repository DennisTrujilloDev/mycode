#!/usr/bin/env python3

import requests
import json

def main():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url).json()
    #json_data = json.dumps(response)
    print(type(response))
    print(response)
   # print(f"Current location:\n" + "lat: " + {response["iss_position"]} + "lon: " )
main()
#{"message": "success", "timestamp": 1664378676, "iss_position": {"latitude": "-51.0570", "longitude": "-156.0218"}}
