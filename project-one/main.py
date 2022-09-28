#!/usr/bin/env python3
"""Alta3 Research | game using python and if logic"""

def main():
    """the main function holds all of our code and is invoked at runtime"""
   
   # prints the title of the game 
    print("\n****************************************")
    print("What Metropolises Suits Your Lifestyle?")
    print("****************************************\n")
    
    # holds user's input in variable user 
    user = input("To get started, please enter your name: \n")

    # The counters are used to keep track of what cities are accruing the most points
    counter_la = 0
    counter_mumbai = 0 
    counter_nyc = 0
    counter_berlin = 0 
    counter_cdmx = 0
    
    # this while loop allows the question to be repeatedly asked until user inputs valid information
    while True:
        # the variable weather is assigned to a lowercase version of the user's input...
        weather = input(f"\n{user}, what's your ideal weather?\nEnter h for hot, w for warm, c for chilly/cold, or v for varied.\n").lower()
        # as long as it falls under one of the conditions stated below. The while loop breaks once one of these conditions is met and the appropriate variable is updated
        if weather == "h":
            counter_mumbai += 1
            break
        if weather == "w":
            counter_cdmx += 1
            counter_la += 1
            break
        if weather == "c":
            counter_berlin += 1
            break
        if weather == "v":
            counter_nyc += 1
            break

    # this while loop allows the question to be repeatedly asked until user inputs a valid response regarding their dietary limitations
    while True:
        # the variable diet is assigned to a lowercase version of the user's input...
        diet = input("\nAre you vegetarian or vegan?\nIf yes, enter y. If no, enter n \n").lower()
        # as long as it falls under one of the conditions stated below. The while loop breaks once one of these conditions is met and the appropriate variable is updated
        if diet == "y":
            counter_mumbai += 1
            counter_berlin += 1
            counter_la += 1
            counter_nyc += 1
            break
        if diet == "n":
            counter_cdmx += 1
            break

    # this while loop allows the question to be repeatedly asked until user inputs a valid response regarding their income
    while True:
         # the variable highincome is assigned to a lowercase version of the user's input...
        highincome = input("\nIs your salary high?\nIf yes, enter y. If no, enter n \n").lower()
        # as long as it falls under one of the conditions stated below. Thewhile loop breaks once one of these conditions is met and the appropriate variable is updated
        if highincome == "y":
            counter_mumbai += 1
            counter_berlin += 1
            counter_la += 1
            counter_nyc += 1
            counter_cdmx += 1
            break
        if highincome == "n":
            counter_cdmx += 1
            counter_berlin += 1
            counter_mumbai += 1
            break

    # this while loop allows the question to be repeatedly asked until user inputs a valid response regarding their preferred mode(s) of transportation
    while True:
        # the variable trans is assigned to a lowercase version of the user's input...
        trans = input("\nHow do you prefer to get around?\nIf by car, enter c. If you prefer public transportation, enter p. \n").lower()
        # as long as it falls under one of the conditions stated below. Thewhile loop breaks once one of these conditions is met and the appropriate variable is updated
        if trans == "c":
            counter_mumbai += 1
            counter_la += 1
            counter_cdmx += 1
            break
        if trans == "p":
            counter_berlin += 1
            counter_nyc += 1
            break

    # this dictionary holds the city names and their respective counter 
    cities = [
            {
                "name": "Mumbai",
                "counter": counter_mumbai
                }, 
            {
                "name": "NYC",
                "counter": counter_nyc
                },
            {
                "name": "LA",
                "counter": counter_la
                },
            {
                "name": "Mexico City",
                "counter": counter_cdmx
                },
            {
                "name": "Berlin",
                "counter": counter_berlin
                }
    ]

    # the counters' values are sorted using sorted() below, where the key argument is used to sort a more complex list by defining city["counter"] as the values that should be used to sort the cities dictionary. Using the keyword lambda saves us time and space.  
    sorted_cities = sorted(cities, key=lambda city: city["counter"])

    # the results from the game are printed using the last two cities in the sorted list.
    print("\n**************************************")
    print(f"A couple cities {user} would enjoy:\n\n{sorted_cities[-1]['name']} & {sorted_cities[-2]['name']}\n\nTime to book those flights!\nFor deals check out\nhttps://matrix.itasoftware.com/search\nThank you for stopping by!")
    print("**************************************\n")

#calling main() using this technique allows others to import your code: 
if __name__ == "__main__":
    main()
