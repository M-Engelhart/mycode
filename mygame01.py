#!/usr/bin/python3

import time

"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      examine [item] (must be in inventory)
      ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                
                },

            'Kitchen' : {
                'north'   : 'Hall',
                'item'    : 'knife',
                'fridge'  : 'Secret Room'       
                },

            'Dining Room' : {
                   'west' : 'Hall',
                   'item' : 'note'
                },

            'Secret Room' : {
                   'item' : 'monster'
                }

           }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

     ## check that the user has the note in their inventory before they can examine it.
    if move [0] == 'examine' :
        if "item" in inventory and move[1] == "note" :
            print("I've been hearing strange noises in the wall behind the fridge. Maybe someone should 'go fridge' and investigate")
        else:
            print("That item is not in your inventory")
            



    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster is going to get you!!')
        counter = 0
        while counter < 5:
            time.sleep(1)
            counter += 1
            user_input = input("Run away!!\n")
            if "go kitchen" in user_input.lower():
                print("You escaped just in time!")
                break
        else:
            print("The monster got you.... Game Over")
            break


#    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
#        print('A monster is going to get you!!')
#        start_time = time.time()
#        while True:
#            user_input = input("Run away!!\n")
#            if "go" in user_input.lower():
#                print("You escaped just in time!")
#                break
#            current_time = time.time()
#            elapsed_time = current_time - start_time
#            if elapsed_time >= 5:
#                print("The monster got you.... Game Over")
#                break            
       

