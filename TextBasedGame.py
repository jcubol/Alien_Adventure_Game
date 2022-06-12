#Josiah Cubol

#Welcome to Defeat the Alien
#Goal: Obtain all 6 items in different rooms throughout the spaceship. You will need ALL 6 items to defeat the Alien or you will lose.
# Sample movement- 'go North', 'get 'item'

# Part 2 Dictionary of dictionaries, like
# text game "Rooms" dictionary:
# The dictionary links a room to other rooms, based on a cardinal direction (N,S,E,W)
# Values: (key) direction --> (value) destination room


def show_instructions():
        print("Move commands: go North, go South, go East, go West")

rooms = {
        'Control Center': {'West': 'Weapons Armory'},
        'Weapons Armory': {'South': 'Main Hold', 'East': 'Control Center'},
        'Main Hold': {'North': 'Weapons Armory', 'South': 'Medical Bay', 'East': 'Crew Quarters',
                      'West': 'Captains Quarters'},
        'Captains Quarters': {'East': 'Main Hold'},
        'Crew Quarters': {'North': 'Cargo Hold', 'West': 'Main Hold'},
        'Cargo Hold': {'South': 'Crew Quarters'},
        'Medical Bay': {'North': 'Main Hold', 'East': 'Engine Room'},
        'Engine Room': {'West': 'Medical Bay'}
        }
print("Keys (rooms): ", *rooms)
print("Values:", *rooms.values())

def move_rooms(direction, room='Control Center'):
    if direction == 'go West':
        room = 'Weapons Armory'
        return rooms






# Josiah Cubol
import time
rooms = {
        'Control Center': {'West': 'Weapons Armory'},
        'Weapons Armory': {'South': 'Main Hold', 'East': 'Control Center'},
        'Main Hold': {'North': 'Weapons Armory', 'South': 'Medical Bay', 'East': 'Crew Quarters',
                      'West': 'Captains Quarters'},
        'Captains Quarters': {'East': 'Main Hold'},
        'Crew Quarters': {'North': 'Cargo Hold', 'West': 'Main Hold'},
        'Cargo Hold': {'South': 'Crew Quarters'},
        'Medical Bay': {'North': 'Main Hold', 'East': 'Engine Room'},
        'Engine Room': {'West': 'Medical Bay'}
        }

direction = ['go North', 'go South', 'go East', 'go West']
location = 'Main Hold'
#carrying = []
#contents = ['Alien', 'Laser Blaster', 'Control Center Key', 'Combat Space Suit', 'Shield', 'Fuel Packet']

def go_new_location(location, direction):
    new_location = location
    for i in rooms:
        if i == location:
            if direction in rooms[i]:
                new_location = rooms[i][direction]

    return new_location
def show_instructions():
    # print a main menu and the commands
    print('-------------------------------------------------------')
    #print("Defeat the Alien Game")
    #print("Collect 6 items to win the game, or be defeated by the invading Alien.")
    print("Move commands: go North, go South, go East, go West")
    #print("Add to Inventory: get 'item name'")
    print('-------------------------------------------------------')

# print('''--------------------------------------------------------------------------------------------------------
# An Alien has invaded your spaceship and plans to kidnap you and your crew once he takes over the ship.
# The spaceship has six items you need to help you defeat the Alien. Save your crew and the save the mission!
# --------------------------------------------------------------------------------------------------------''')

time.sleep(4)
show_instructions()
time.sleep(4)
def go_new_location(location, direction):
    new_location = location
    for i in rooms:
        if i == location:
            if direction in rooms[i]:
                new_location = rooms[i][direction]

    return new_location

while 1:
    print('You are in', location)
    direction = input('Which direction would you like to go?').strip()
    if direction == 'Exit':
        exit(0)

    if direction == 'North' or 'South' or 'West' or 'East':
        new_location = go_new_location(location, direction)

        if new_location == location:
            print('You cant go that way, please choose a new direction!')
        else:
            location = new_location
    else:
        print('Invalid entry!')