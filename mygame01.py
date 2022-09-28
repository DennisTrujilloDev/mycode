#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

#import third party modules
import random 
import crayons

def main():
    def showInstructions():
        """Show the game instructions when called"""
    
        #print a main menu, commands, context and instructions
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
    
        # states it if there's an entity in the room 
        if 'entity' in rooms[currentRoom]:
            print(crayons.red(rooms[currentRoom]['entity'] + ': "RAWR!"\nQuick -- you MUST hide (command: hide now)\nbefore moving on to the next room!'))
        # if there isn't an entity in the room 
        else:
            print(crayons.cyan('"Hmmm.. it seems the room is empty."'))
            print(crayons.yellow('Possible direction commands:'))
            # if east is in the available directions for that room  
            if 'east' in rooms[currentRoom]:
                print(crayons.yellow('    go east'))
            #if north is in the available directions for that room  
            elif 'north' in rooms[currentRoom]:
                print(crayons.yellow('    go north'))
            # if west is in the available directions for that room 
            elif 'west' in rooms[currentRoom]:
                print(crayons.yellow('    go west'))
            #if south is in the available directions for that room 
            elif 'south' in rooms[currentRoom]:
                print(crayons.yellow('    go south\ln'))
    
        # print the number of lives and moves available 
        print(crayons.green('\nRemaining...'))
        print('Live(s):', health-1)
        print('Hide command(s):', hidecount)
        print('Ouija session(s):', ouijacount)
        print(crayons.blue('******************************'))
        print()

    # these counters are used to keep track of how many moves/lives the user has remaining
    ouijacount = 2
    hidecount = 4
    health = 2

    # the variable is set to Lobby in order to start the user off in the lobby
    currentRoom = 'Lobby'

    #invoke function that shows instructions
    showInstructions()

    # dictionary linking rooms together and placing entities in rooms 
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

    # breaking this while loop means the game is over.
    while True:
        #invokes function that shows status 
        showStatus()

        # The player MUST type something in. Otherwise, input will keep asking for user input. The strip method is used here to trim spaces from user input
        move = ''
        while move == '':  
            move = input('>').strip()

        # normalizing input:
        # .lower() makes it lower case, .split() turns it to a list
        # therefore, "get golden key" becomes ["get", "golden key"]          
        move = move.lower().split(" ", 1)

        # if they type 'go' first
        if move[0] == 'go':
            # if the user has typed go first and the second word (direction) is not in the list of directions available for that room... 
            if move[1] not in rooms[currentRoom]:
                print("Sorry, youre input is invalid.\nPlease ensure\nyou have avoided any entities in the\nroom (if any) before exiting.")
            # if the user inputs a direction that is valid and the entity is not present in the room...
            elif move[1] in rooms[currentRoom] and "entity" not in rooms[currentRoom]:
                # the current room variable is reassigned to the new room
                currentRoom = rooms[currentRoom][move[1]]
            # if the user inputs a valid direction but the entity hasn't been avoided
            elif move[1] in rooms[currentRoom] and "entity" in rooms[currentRoom]:
                print("Please try to avoid the dark entity\n(command: hide now) before continuing\non to the next room.")
        #if they type 'play' then 'ouija' and they have available moves for playing ouija
        if move[0] == 'play' and move[1] == 'ouija' and ouijacount <= 2 :
            # the number of ouija moves available is decreased by one
            ouijacount -= 1
            # ask user what they'd like to communicate to the entities
            input("What would you like to say to the entities?\n")
            # play a round of ouija using randint to generate two random integer values
            entity = random.randint(0, 10)
            user = random.randint(0, 10)
            # if the user's random int is greater than or equal to the entity's
            if user >= entity:
                print("You have distracted them!\nYou've gained 1 life.")
                #the user gains a life
                health += 1
            # if the user's random int is less than or equal to the entity's
            else:
                print("You're upsetting them angry!\nRAWR RAWR\nYou've lost 2 lives.")
                # the user loses 2 lives
                health -= 2
        # if the user wants to play ouija but they have run out of ouija moves
        elif move[0] == 'play' and move[1] == 'ouija' and ouijacount >= 2 :
            print("Sorry, you've run out of ouija rounds...")

        # if there is no entity in the room but the user chose to try to hide from an entity
        if 'entity' not in rooms[currentRoom] and move[0] == 'hide':
            print("There either arent any dark entities\nin here or you've already avoided them.\nMove along, now.")

    # If a player enters a room with an entity
        if 'entity' in rooms[currentRoom]:
            # if the user tries to hide and they have moves in order to be able to do so
            if move[0] == 'hide' and move[1] == 'now' and hidecount <= 4 :
                # the number of hide oves available decreases by 1 
                hidecount -= 1
                # randint is used to generate two random values
                entity = random.randint(0, 10)
                user = random.randint(0, 10)
                # if the user's random int is greater than or equal to the entity's
                if user >= entity:
                    print("You hid from the entity -- good going!")
                # if the user's random int is less than or equal to the entity's
                else:
                    print("Ouch, that one hurt!")
                    # user's health decreases by 1
                    health -= 1
                # the entity is removed from the dictionary regardless of whether they have successfully avoided the entity or not 
                del rooms[currentRoom]['entity']
       
       # if entity is present but the user doesn't have any ouija or hide moves left 
            elif hidecount <= 0 and ouijacount <= 0 :
                print("GAME OVER. Evil got it's way...")
                # the while loop is broken and the game ends
                break
    
        # if the user has run out of lives
        if health <= 0:
            print("0 Lives remaining. You're stuck\nhere forever. Goodbye!")
            # the game ends via breaking the while loop
            break
    
        #if the user has made it to the backyard, they have won
        if currentRoom == 'Backyard':
            print('Phew... that was close! Congratulations --\nyou made it out of the Haunted Hotel!')
            #the while loop breaks, ending the game
            break

# calling main() using this technique allows others to import your code: 
if __name__ == "__main__":
    main()
