#!/usr/bin/python3

import pandas as pd

classinfo = {
    "all": [
        {
            "name": "Aaron",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Alexandra",
            "skill level": "admirable",
            "spirit animal": "Shark",
            "super power": "Super Strength",
        },
        {
            "name": "Alice",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Weather Control",
        },
        {
            "name": "Angela",
            "skill level": "astonishing",
            "spirit animal": "Banana",
            "super power": "Flight",
        },
        {
            "name": "Ayrat",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "X-ray Vision",
        },
        {
            "name": "Blake",
            "skill level": "brilliant",
            "spirit animal": "Eagle",
            "super power": "Shape of: A Giant Shark",
        },
        {
            "name": "Brandon",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Invisibility",
        },
        {
            "name": "Carl",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Transformation",
        },
        {
            "name": "Chris",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Pyrokinesis",
        },
        {
            "name": "Christian",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Invulnerability",
        },
        {
            "name": "Deepak",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Explosive Shouts",
        },
        {
            "name": "Dennis",
            "skill level": "great",
            "spirit animal": "Pigeon",
            "super power": "Matter Ingestion",
        },
        {
            "name": "Felicia",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Zoolingualism",
        },
        {
            "name": "Gabriel",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Height Manipulation",
        },
        {
            "name": "Julian",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Hydrokinesis",
        },
        {
            "name": "Kelly",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Lashay",
            "skill level": "phenomenal",
            "spirit animal": "Leopard",
            "super power": "Stretchy",
        },
        {
            "name": "Nabin",
            "skill level": "pleasant",
            "spirit animal": "Albatross",
            "super power": "Steel Skin",
        },
        {
            "name": "Pratibha",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Teleportation",
        },
        {
            "name": "Quentin",
            "skill level": "remarkable",
            "spirit animal": "Lynx",
            "super power": "Polyglot",
        },
        {
            "name": "Will",
            "skill level": "super",
            "spirit animal": "Fox",
            "super power": "Eat Anything",
        },
    ]
}

def main():
    print("P1:" + classinfo["all"][11]["name"])
    print("P2: My name is " + classinfo["all"][11]["name"] +  " and my spirit animal is a " + classinfo["all"][11]["spirit animal"])
    for i in range(20):
        print (classinfo["all"][i]["name"] + ", a " + classinfo["all"][i]["skill level"].lower() + " " + classinfo["all"][i]["spirit animal"].lower() + " of a programmer, possesses a " + classinfo["all"][i]["super power"].lower() + " factor for moonlighting as a hero!" )
main()
