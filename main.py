print("Welcome to Escape Room! \n To learn how to play type tutorial, chose a map!\n the office\n")
user_input = input()
if user_input == "tutorial":
    import tutorial

elif user_input == "the office":
    import office

else:
    print("that is not a command")