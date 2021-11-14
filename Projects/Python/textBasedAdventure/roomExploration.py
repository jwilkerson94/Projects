# a text based adventure
# character uses commands to go through the rooms

import time

# time after messages
delay = 0.5

# win message
def win():
    time.sleep(delay)
    print("You win!")

# kill the player
def kill():
    time.sleep(delay)
    print("You died!")

# various rooms
def diningroom():
    room_builder([False, True] , 'The dining room', True, ["kill", "win"])

def kitchen():
   room_builder([False, True] , 'The kitchen', False, ["kill", "diningroom"])

def nook():
    room_builder([False, True] , 'The nook', True, ["kill", "win"])

def bathroom():
    room_builder([True, False] , 'The bathroom', True, ["win", "kill"])

def bedroom():
    room_builder([True, False] , 'The bedroom', False, ["bathroom", "kill"])

def office():
    room_builder([True, False] , 'The office', False, ["nook", "kill"])

# shows room
def room_builder(room_list, room_name, is_end_room, next_rooms):
    print(f"You have just entered {room_name}.")
    time.sleep(delay)
    room_count = len(room_list)
    choices = []

    # input message based on number of doors
    input_message = "Choose a door: ("
    # add each door name to the list of choices
    door_message = ""
    for count in range(room_count):
        choices.append(f"door {count + 1}")
        if  count + 1 < room_count:
            door_message += f"door {count + 1}, "
        else: 
            door_message += f"door {count + 1}) " 
    
    # add to input_message
    input_message += door_message
    time.sleep(delay)

    while True:
        command = input(input_message).lower()

        if command in choices:
            if room_list[choices.index(command)]:
                if is_end_room:
                    time.sleep(delay)
                    print("You have chosen wisely")
                    win()
                    break
                else:
                    time.sleep(delay)
                    print("Please proceed to the next room.")
                    time.sleep(delay)
                    eval(next_rooms[choices.index(command)] + "()")
                    break
            else:
                kill()
                break
        else:
            time.sleep(delay)
            print(f"Sorry, you must enter ({door_message}")


room_builder([True, True, True], 'The Entrance Hall', False, ["kitchen", "bedroom", "office"])