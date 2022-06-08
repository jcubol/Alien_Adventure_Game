# Josiah Cubol
import time
rooms = {
        'Control Center': {'West': 'Weapons Armory', 'contents': ['Alien'],
                           'text': 'The Control Center. The alien is here! Are you ready to fight?'},
        'Weapons Armory': {'East': 'Control Center', 'South': 'Main Hold', 'contents': ['Laser Blaster'],
                           'text': 'Weapons Armory. There is a Laser Blaster in the weapons locker'},
        'Main Hold': {'North': 'Weapons Armory', 'West': 'Captains Quarters', 'East': 'Crew Quarters',
                      'South': 'Medical Bay', 'contents': [], 'text': 'Main Hold. Begin your Quest'},
        'Captains Quarters': {'East': 'Main Hold', 'contents': ['Control Center Key'],
                              'text': f"The Control Center Key is on the captain's desk!"},
        'Crew Quarters': {'West': 'Main Hold', 'North': 'Cargo Hold', 'contents': ['Combat Space Suit'],
                          'text': 'The Crew Quarters. Your spacesuit lying on your bunk bed'},
        'Cargo Hold': {'South': 'Crew Quarters', 'contents': ['Shield'], 'text': 'A shield is on the wall.'},
        'Medical Bay': {'North': 'Main Hold', 'East': 'Engine Room', 'contents': 'Fuel Packet',
                        'text': 'There is a fuel packet on the table.'},
        'Engine Room': {'West': 'Medical Bay', 'contents': ['Oxygen Tank'],
                        'text': 'A spare oxygen tank is in the corner of the engine room.'}
}
directions = ['North', 'South', 'East', 'West']
currentRoom = rooms['Main Hold']
carrying = []
contents = ['Alien', 'Laser Blaster', 'Control Center Key', 'Combat Space Suit', 'Shield', 'Fuel Packet']

def show_instructions():
    # print a main menu and the commands
    print('-------------------------------------------------------')
    print("Defeat the Alien Game")
    print("Collect 6 items to win the game, or be defeated by the invading Alien.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get 'item name'")
    print('-------------------------------------------------------')

print('''--------------------------------------------------------------------------------------------------------
An Alien has invaded your spaceship and plans to kidnap you and your crew once he takes over the ship.
The spaceship has six items you need to help you defeat the Alien. Save your crew and the save the mission!
--------------------------------------------------------------------------------------------------------''')
time.sleep(4)
show_instructions()
time.sleep(4)
while True:
    # display current location
    print()
    print('You are in {}.'.format(currentRoom['text']))
    # get user input
    command = input('\nWhat do you do? ').strip()
    # movement
    if command in directions:
        if command in currentRoom:
            currentRoom = rooms[currentRoom[command]]
        else:
            # bad movement
            print("Look's like you can't go that way.")
    # quit game
    elif command.lower() in ('q', 'quit'):
        break
    # bad command
    elif command.lower().split()[0] == 'get':
        item = command.lower().split()[1]
        if item in currentRoom['contents']:
            carrying.append(item)
            print('You acquired {}.'.format(currentRoom['contents']))
        else:
            print("That item isn't here.")
    if command in currentRoom:
        currentRoom = rooms[currentRoom[command]]
    if currentRoom in ['Control Center']:
        if len(carrying) == 6:
            print('You collected all of the items and defeated the Alien! You saved your crew members and the mission!')
        else:
            print('It looks like you have not found everything, you have been defeated!')

