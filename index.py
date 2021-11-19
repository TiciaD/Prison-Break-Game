# Monticia Dunn
# Prison Break Game
rooms = {
# Declare rooms where everything is
    'Your Cell': {'North': 'Corridor', 'West': 'Yard', 'East': 'Laundry', 'South': 'Security'},
    'Corridor': {'East': 'Roy\'s Cell', 'South': 'Your Cell', 'Item': 'stash of cash'},
    'Roy\'s Cell': {'West': 'Corridor', 'Item': 'shank'},
    'Laundry': {'North': 'Kitchen', 'West': 'Your Cell', 'Item': 'towels'},
    'Kitchen': {'South': 'Laundry', 'Item': 'spoons'},
    'Security': {'North': 'Your Cell', 'East': 'Visitation', 'Item': 'keys'},
    'Visitation': {'West': 'Security', 'Item': 'phone'},
    'Yard': {'East': 'Your Cell', 'Item': 'villain'}
}
current_room = 'Your Cell'
# function for moving from room to room
def move_room(current_room, direction):
    new_room = current_room
    # declare new room is now the current room
    for i in rooms:
        if i == current_room:
            if direction in rooms[i]:
                new_room = rooms[i][direction]
                # assigning new room
    return new_room
# return the new room player will be in

# This function is used to display items in the room
def get_item(current_room):
    if 'Item' not in rooms[current_room]:
        return 'Nothing'
# If the Item isn't in the room, returns 'Nothing' response
    else:
        return rooms[current_room]['Item']
    #If it is in the room, returns Item value

#This function shows an introduction and instructions when the game starts
def intro():
    print("Welcome to Meth Bay Penitentiary.")
    print("You have been organizing an elaborate prison break plan with your cellmate Gene for the past few months.")
    print("Today is the day to make it happen! You have been digging a tunnel in your cell to escape to the Yard ")
    print("from there you will need various items to complete your escape.")
    print("You and Gene will need to gather everything before attempting to leave ")
    print("or else the whole plan might be at risk! ")
    print("Use the commands below to move between rooms and collect the items you need:")
    print()
    print("Instructions: Move between rooms to collect items")
    print("Moves: go north, go south, go east, go west")
    print('Pick up item: get "item name"')
    print('Quit: Type "quit" to quit the game')
    print('You and Gene start off in Your Cell discussing where to head to first before heading West towards the Yard.')
    input('\nPress the <ENTER> key to continue...')
    # pauses game until player presses ENTER so they can read the prompt

intro()
#calling function for introduction and instructions
inventory = []

while (1):  # gameplay loop
    item = get_item(current_room)  # calling get_item function to display item to user
    # Different scenarios depending on item encountered for story purposes
    if item in inventory:  # if player has already collected the item from a room
        pass  # it will not display the item in the room
    elif item == 'stash of cash':
        print('As you walk along the corridor Gene points out the crevice you left your STASH OF CASH in.')
    elif item == 'keys':
        print('As you sneak into the Security room, Gene distracts the guards while '
              'you spot the KEYS near the door.')
    elif item == 'towels':
        print('Gene mentions you need a rope, as you pass through the laundry you spot '
              'some TOWELS you could tie together.')
    elif item == 'spoons':
        print('The tunnel still needs a little more digging to get to the yard, '
              'Gene suggests grabbing more SPOONS from the kitchen.')
    elif item == 'phone':
        print('Gene\'s cousin has arrived in visitation, he smuggles in a PHONE for you two.')
    elif item == 'shank':
        print('Gene tries to talk Roy into coming but Roy seems suspicious of Gene, '
              'he slyly hands you a SHANK.')
    elif item == 'villain': #if
        print('You\'re still missing something... You failed to escape the Yard.')
        exit(0)
    else:
        if item in inventory:  # if player has already collected the item from a room
            pass  # it will not display the item in the room
    print('You are currently in ', current_room)  # printing current room player is in
    print('Inventory:', inventory)  # printing inventory

    direction = input("Enter 'go North/South/East/West' or 'Exit': ")  # asking user to input direction
    if direction == 'go East' or direction == 'go West' or direction == 'go North' or direction == 'go South':  # if
        direction = direction[3:]
        new_room = move_room(current_room, direction)  # calling function for moving rooms
        if new_room == current_room:  # if player inputs wrong direction
            print()
            print("You can't go that way!")
            print()
        else:
            current_room = new_room  # changing current room value to new room value
    elif direction == str('get ' + item):  # if player tries to pick up an item
        if item in inventory:  # if item already  in inventory
            print('You already collected ' + item + ' from this room.')
        else:
            print("You collected " + item + "!")
            inventory.append(item)  # appending inventory with new item player picked up
    else:
        print('Invalid direction!!')  # if player enters invalid input

    if len(inventory) == 6:  # if player collects all 6 items before entering the Yard, they win
        print()
        print('                   Congratulations you collected all 6 items!                ')
        print('You and Gene rush back to Your Cell to finish tunneling with the spoons into the Yard.')
        print('Once in the Yard you both sprint for the gate and use the keys to '
              'get through the security only door')
        print('Now you only have one more wall before freedom, '
              'Gene ties the towels together to help you get over the wall.')
        print('Once over you use the phone to call a ride you set up with your brother')
        print('As soon as you hang up, Gene sucker punches you and takes the phone and the stash of cash')
        print('Roy warned you about this, luckily you have the shank and after wrestling for a while,'
              'you have to stab one of your best friends to make it out alive.')
        print()
        break  # break gameplay loop and continue to quit game loop