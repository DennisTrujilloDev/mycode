#!/usr/bin/python3

import requests

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()
    print(pokemon)
    #transforms json data to python so it converts to dict
    #project 3 what comes back from api usually json, as part of project, nromalize it into python data or use pandas to transform to readable
    #ok for data to come back with single quotes b/c its pythonic data 
    # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        # Display the value associated with 'name'
        #print(poke["name"])
        print(poke.get("name"))

    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")

if __name__ == "__main__":
    main()

