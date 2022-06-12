#Josiah Cubol
import time
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
}

direction = ['North', 'South', 'East', 'West']
location = 'Great Hall'

def show_instructions():
    print('-------------------------------------------------------')
    print("Move commands: North, South, East, West.")
    print("Enter Exit to exit the game.")
    print('-------------------------------------------------------')


time.sleep(2)
show_instructions()
time.sleep(2)


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


#Code is good. Need to figure out how to put anything outside of directions and exit as invalid entry+