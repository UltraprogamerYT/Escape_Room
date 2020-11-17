print("welcome to the escape room tutorial\n this is a simple game with simple commands, it is most fun when played with friends, here are all the commands!\n look (direction) \n inspect(item) \n use (item) with (item)\n here is an example!\n look left:you look left and see a drawer/ inspect drawer:you look in the drawer and find a key/\n use key with door:you put the key in the door and escape!\n this is a trickey game and there may be many sequences before you get the final key\n good luck and most importantly have fun\n type return to go back to the main screen ")
user_input = input()
if user_input == "return":
    import main
