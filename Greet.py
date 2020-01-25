name = input("Please enter your name ")


def greet():
    print("Hello " + name)
    print("How are you? ")
    greeting = input("If your are fine type 'Y' else type 'N' ")
    if greeting == "Y" or greeting == "y":
        print("That's great to hear! :) ")
    elif greeting == "N" or greeting == "n":
        print("Sorry to hear that :( ")
    else:
        print("ERROR : Invalid input run program again! ")


greet()
