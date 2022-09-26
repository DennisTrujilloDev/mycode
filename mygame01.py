#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import random 
import crayons

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    

    ========The Haunted Hotel========

    Goal: Starting in the lobby, you will make your
    way through the hotel's rooms. Hide to avoid the
    entities often reported to haunt the Haunted 
    Hotel's eerie rooms. Make it to the backyard
    to win!
    
    Commands:
        go [direction] e.g. go north, go south
        play ouija
        hide now

   -------------------------------------------

    1. To move from one room to the next
        (4 commands: go east, go west, go 
        south, go north) you must first 
        try to avoid the evil entity (if any, 
        command: hide now) present in
        the current room.
    2. If you fail to sneak past the enemy, it
        attacks and you lose a life.
   
   -------------------------------------------

    3. You may choose to communicate with the
        entities at any point (command: play
        ouija). You can choose to play a round
        of ouija at any point a maximum of 2 times.
    4. If your message seems to distract these
        dark entities, you gain an extra life.
        If your words irritate them, you lose 
        2 lives. 
    5. If you run out of lives (user has 2 lives
        total) or run into an evil entity without
        any hide moves left (maximum is 4)...
        enjoy your new home.

        ========MUA HA HA HA========
   
   -------------------------------------------
    '''
    )

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print(crayons.blue('******************************'))
    print('You are in the following room: ' + crayons.green(currentRoom))
    if 'entity' in rooms[currentRoom]:
        print(crayons.red(rooms[currentRoom]['entity'] + ': "RAWR!"\nQuick -- you MUST hide (command: hide now)\nbefore moving on to the next room!'))
    else:
        print(crayons.cyan('"Hmmm.. it seems the room is empty."'))
        print(crayons.yellow('Possible direction commands:'))
        if 'east' in rooms[currentRoom]:
            print(crayons.yellow('    go east'))
        elif 'north' in rooms[currentRoom]:
            print(crayons.yellow('    go north'))
        elif 'west' in rooms[currentRoom]:
            print(crayons.yellow('    go west'))
        elif 'south' in rooms[currentRoom]:
            print(crayons.yellow('    go south\ln'))
    print(crayons.green('\nRemaining...'))
    print('Live(s):', health-1)
    print('Hide command(s):', hidecount)
    print('Ouija session(s):', ouijacount)
    print(crayons.blue('******************************'))
    print()

#COUNTERS
ouijacount = 2
hidecount = 4
health = 2
currentRoom = 'Lobby'

#invoke function that shows instructions
showInstructions()

# dictionary linking a room to other 
rooms = {
        
            'Lobby' : {
                'east' : 'Room 113',
                'west': 'Room 138'      
            },
            "Dark passage": { 
                "east": "Kitchen",
                "west": "Blood-filled Pool",
                "entity": "rabid dog"
            },
            "Room 113": { 
                "north": "Dark passage",
                "entity": "evil spirit" 
            },
            "Room 138": {
                "north": "Dark passage",
                "entity": "savage Pete"
            },
            "Blood-filled Pool": {
                "north": "Room 132"
            },
            "Room 132": {
                "north": "Dungeon",
                "entity": "vampiric mermaid"
            },
            "Dungeon": {
                "east": "Backyard",
                "entity": "evil spirit"
            },
            "Kitchen": {
                "north": "Crawl space",
                "entity": "knight"
            },
            "Crawl space": {
                "north": "Room 117"
            },
            "Room 117": {
                "west": "Backyard",
                "entity": "Freddy Krueger"
            },
            "Backyard": { 
            },
    }

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>').strip()

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        if move[1] not in rooms[currentRoom]:
            print("Sorry, there aren't any rooms\nin that direction. Please ensure\nyou have avoided any entities in the\nroom (if any) before exiting.")
        #check that they are allowed wherever they want to go
        elif move[1] in rooms[currentRoom] and "entity" not in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        elif move[1] in rooms[currentRoom] and "entity" in rooms[currentRoom]:
            print("Please try to avoid the dark entity\n(command: hide now) before continuing\non to the next room.")
            
    #if they type 'play' first
    if move[0] == 'play' and move[1] == 'ouija' and ouijacount <= 2 :
        ouijacount -= 1
        # 1. Ask user what they'd like to say to the entities
        input("What would you like to say to the entities?")
        # 2. play round of ouija (more or less health)
        entity = random.randint(0, 10)
        user = random.randint(0, 10)
        if user >= entity:
            print("You have distracted them!\nYou've gained 1 life.")
            health += 1
        else:
            print("You're upsetting them angry!\nRAWR RAWR\nYou've lost 2 lives.")
            health -= 2
    elif move[0] == 'play' and move[1] == 'ouija' and ouijacount >= 2 :
        print("Sorry, you've run out of ouija rounds...")


    if 'entity' not in rooms[currentRoom] and move[0] == 'hide':
        print("There either arent any dark entities\nin here or you've already avoided them.\nMove along, now.")

## If a player enters a room with an entity
    if 'entity' in rooms[currentRoom]:
      #  print("There's something in here... you must hide!")
        #NEW: if user inputs flee
        #NEW: play a round of flee
        if move[0] == 'hide' and move[1] == 'now' and hidecount <= 4 :
            hidecount -= 1
            entity = random.randint(0, 10)
            user = random.randint(0, 10)
            if user >= entity:
                print("You hid from the entity -- good going!")
                #delete entity
                del rooms[currentRoom]['entity']
            else:
                print("Ouch, that one hurt!")
                health -= 1
                del rooms[currentRoom]['entity']
        elif hidecount <= 0 and ouijacount <= 0 :
            print("GAME OVER. Evil got it's way...")
            break
    if health <= 0:
        print("0 Lives remaining. You're stuck\nhere forever. Goodbye!")
        break
    ## Define how a player can win
    if currentRoom == 'Backyard' and health >= 0:
        print('Phew... that was close! Congratulations --\nyou made it out of the Haunted Hotel!')
        break
