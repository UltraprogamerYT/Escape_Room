print("\n \n you wake up on a soft floor, you feel very tired and and your memory is a blurr. \n you get up to look around, once you realaze that you are alone, you start yelling for help \n but no one is here to help you, you must find a way to escape")
inventory = {}
# main game loop-----------------------------------------------------------------------------------------
while True:
    player_input = input("What whould you like to do?: ")
    if player_input == ("look up"):
        print("\nyou look up and see a normal roof, there is nothing here")

    elif player_input == ("look left"):
        print("\nYou look left and see a large desk with tall stacks of paper and a laptop")

    elif player_input == "look right":
        print(
            "\nyou look right and see a safe sitting on the ground, you try to open it but it is locked \n you need to find the code, you also see a picure frame with a picture of a man and a little girl right above it")

    elif player_input == ("look down"):
        print("\n you look down and see a carpet floor, but to the corner you see a loose carpet in the corner")

    elif player_input == "look forward":
        print("\n you look forward and see a door, you try tugging the doorknob but nothing happens")

    elif player_input == "look behind":
        print(" \n you look behind you and see a small door, must be storage")

    # inspect game loop -----------------------------------------------------------------------------------
    elif player_input == "inspect picture":
        print("\n you pick up the picture and look closeley, nothing normal, but after you flipped it over it read this: time with my dauter, may7 2016\n but there is something in the back, you need a knife")

    elif player_input == ("inspect small door"):
        print("\nyou look inside but it is too dark to see anything and you step on something, you must find a flashlight")

    elif player_input == ("inspect desk"):
        print("\nyou look through the desk but you found nothing, however there is a number lock on one of them")
        desk_code = input("what do you think is the code")
        if desk_code == ("572016"):
            print("\nyou type in the code and you hear a click, you pull the door open, you see personal files and a swiss army knife!\n you put the knife in your pocket and contenue")
            inventory['swiss army knife'] = 1

        else:
            print("you type in the code and and nothing happens, you pull the handle, nothing, try again!")


    elif player_input == ("inspect safe"):
        if inventory == "key":
            print("you put the key in the safe and pull it open, you see personal papers and a flashlight!, you put the flashlight in your pocket and close the safe door")
            inventory['flashlight'] = 1
        else:
            print("you need a flashlight to do this")



    elif player_input == ("use flashlight with small door"):
        if inventory == "flashlight":
            print("you turn on the flashlight and look around, you see a large key that says SPEARE\n you put the key in your pocket and close the door")
            inventory['Spare Key'] = 1


    elif player_input == ("use knife with painting"):
        if inventory == "knife":
            print("You cut the back open and it reveals a key, you put the key in you pocket and replace the photo")
            inventory['key'] = 1
        else:
            print("you need a knife to open this")

    elif player_input == ("use spare key with door"):
        if inventory == "Spare Key":
            print("you unlock the juant door and run to safety \n good job, you have escaped!")

    elif player_input == '':

        pass

    elif player_input == 'inventory' or player_input == 'inv':
        print('You look inside your inventory, and you see these items:\n')
        for x in inventory:
            print(inventory[x], x)
    else:
        print('That is not a command')
