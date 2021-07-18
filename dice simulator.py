import random

print("******This is a Dice Simulator******")

x="y"
while x=="y":
    number=random.randint(1,6)

    if number==1:
        print(" _________")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("|_________|")

    if number==2:
        print(" __________")
        print("|          |")
        print("|O        O|")
        print("|          |")
        print("|__________|")

    if number==3:
        print(" __________")
        print("|O         |")
        print("|    O     |")
        print("|         O|")
        print("|__________|")

    if number==4:
        print(" __________")
        print("|O        O|")
        print("|          |")
        print("|O        O|")
        print("|__________|")

    if number==5:
        print(" ____________")
        print("|O         O|")
        print("|    O      |")
        print("|O         O|")
        print("|___________|")

    if number==6:
        print(" ___________")
        print("|O        O |")
        print("|O        O |")
        print("|O        O |")
        print("|___________|")

    x=input("*****press y or  n to roll again*****")    