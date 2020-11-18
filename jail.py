print("you wake up on the ground unconsious of where you are \n or what your name is \n then you realize that you are in a prizon cell. \n you have never broken the law before.\n imiediatley you get up with panic and start banging on the doors\n as the last of your energy is drained you sit down \n there is no one here, you must escape on your own \n commands include look up down left or right \n and to inspect an object do inspect OBJECT")
inventory = {}
# Main Game Loop
while True:

    # inputs
    player_input = input("")
    print("What whould you like to do?")



    if player_input == ("look up"):
        print(" \n you look up, very high up is a loose vent \n you try to reach it but it is too high up")

    elif player_input == ("look down"):
        print(" \n you look down and see that the floor is made of bricks \n and to your surprise you see a lose brick")

    elif player_input == ("look back"):
        print(" \n you look behind and you see a bed and started wondoring why the bed was so close to the toilet")

    elif player_input == ("look right"):
        print(" \n you look right and see a toilet, a sink, and a mirror, you look in the mirror \n you look like you havent had a shower in days \n you dig in your pocket and find a hair comb and you comb your hair")

    elif player_input == ("look left"):
        print("you look left and see an empty wall")
    elif player_input == ("inspect brick"):
        print(" \n you pull out the brick and to your surprise there is a wrench in there \n you pull out the wrench and slide the brick back in place")
        print(" \n wrench has been added to your inventory")
        inventory['wrench'] = 1

    elif player_input == ("inspect loose vent"):
        print(" \n the lose vent is too high up to reach")

    elif player_input == ("inspect bed"):
        print(" \n you lay on the bed and you feel something hard and sharp in the pillow \n you dump the contents out of the pillow cover and find \n a swiss army knife and a nail file")
        print(" \n you also find a jail outfit under the bed")
        print("\n nail file, swiss army knife, and jail outfit have been added into your inventory")
        inventory['nail file'] = 1
        inventory['knife'] = 1
        inventory['jail outfit'] = 1


    elif player_input == ("inspect sink"):
        print("you turn the knobs on the sink and no water flows, you look under the sink and see a valve \n that can be tightened by a wrench")

    elif player_input == ("inspect door"):
        print("you look closely at the door and realized that it is solid metal, you must find anothor way to escape")

    elif player_input == ("inspect toilet"):
        print("you flush the toilet and nothing happens, you look in the water reserve and it is empty")


    elif player_input == ("use wrench with sink"):
        if inventory == "wrench":
            print("you have your wrench in hand, but what way do you turn it?")
            if player_input == "up up down up":
                print("you twist the wrench and you hear water flowing, you look in the toilet bowl and see water \n you wash your face in the sink")
            else:
                print("you turn the wrench but nothing happens try again!")


    elif player_input == '':

        pass

    elif player_input == 'inventory' or player_input == 'inv':
        print('You look inside your inventory, and you see these items:\n')
        for x in inventory:
            print(inventory[x], x)
    else:
        print('That is not a command')