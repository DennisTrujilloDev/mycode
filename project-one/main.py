#!/usr/bin/env python3
"""COMMENT HERE"""
print("'What Metropolises Suits Your Lifestyle?'")
user = input("To get started, please enter your name: \n")

#COUNTERS
counter_LA = 0
counter_Mumbai = 0 
counter_NYC = 0
counter_Berlin = 0 
counter_CDMX = 0

#WEATHER
weather_pref = ["h", "w", "c", "v"]
weather = input(f"{user}, what's your ideal weather? Enter h for hot, w for warm, c for chilly/cold, or v for varied.\n").lower()

while True:
    if weather not in weather_pref:
        weather = input(f"{user}, what's your ideal weather? Enter h for hot, w for warm, c for chilly/cold, or v for varied.\n").lower()
    elif weather == "h":
        counter_Mumbai += 1
        break
    elif weather == "w":
        counter_CDMX += 1
        counter_LA += 1
        break
    elif weather == "c":
        counter_Berlin += 1
        break
    elif weather == "v":
        counter_NYC += 1
        break

#DIET
diet = input("Are you vegetarian or vegan? If yes, enter y. If no, enter n \n").lower()
diet_validation = ["y", "n"]
while True:
    if diet not in diet_validation:
        diet = input("Are you vegetarian or vegan? If yes, enter y. If no, enter n \n").lower()
    elif diet == "y":
        counter_Mumbai += 1
        counter_Berlin += 1
        counter_LA += 1
        counter_NYC += 1
        break
    elif diet == "n":
        counter_CDMX += 1
        break

#INCOME
highincome = input("Is your salary high? If yes, enter y. If no, enter n \n").lower()
income_validation = ["y", "n"]
while True:
    if highincome not in income_validation:
        highincome = input("Is your salary high? If yes, enter y. If no, enter n \n").lower()
    elif highincome == "y":
        counter_Mumbai += 1
        counter_Berlin += 1
        counter_LA += 1
        counter_NYC += 1
        counter_CDMX += 1
        break
    elif highincome == "n":
        counter_CDMX += 1
        counter_Berlin += 1
        counter_Mumbai += 1
        break

#TRANSPORTATION
trans = input("How do you prefer to get around? If by car, enter c. If you prefer public transportation, enter p \n").lower()
trans_validation = ["c", "p"]
while True:
    if trans not in trans_validation:
        trans = input("How do you prefer to get around? If by car, enter c. If you prefer public transportation, enter p. \n").lower()
    elif trans == "c":
        counter_Mumbai += 1
        counter_LA += 1
        counter_CDMX += 1
        break
    elif trans == "p":
        counter_Berlin += 1
        counter_NYC += 1
        break

#results
cities = [{"name": "Mumbai", "counter": counter_Mumbai}, {"name": "NYC", "counter": counter_NYC}, {"name": "LA", "counter": counter_LA},{"name": "Mexico City", "counter": counter_CDMX}, {"name": "Berlin", "counter": counter_Berlin}]
sorted_cities = sorted(cities, key=lambda d: d["counter"])
#above line
print(sorted_cities)
print(f"A couple cities {user} would enjoy:\
{sorted_cities[-1]['name']}\
& {sorted_cities[-2]['name']}\
Time to book those flights!\
For deals check out https://matrix.itasoftware.com/search\
Thank you for stopping by!")
