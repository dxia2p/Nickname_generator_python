import random

firstName = input("Enter your first name")
lastName = input("Enter your last name")
nicknames = ["The Bulldog"]

def DisplayMenu():
    print(f"MAIN MENU ({firstName} {lastName})")
    print("1. Change Name")
    print("2. Display a Random Nickname")
    print("3. Display all Nicknames")
    print("4. Add a Nickname")
    print("5. Remove a Nickname")
    print("6. Exit")
    return int(input("Enter #"))

inp = DisplayMenu()
while inp != 6:
    match inp:
        case 1:
            print("CHANGE NAME")
            firstName = input("Enter your first name")
            lastName = input("Enter your last name")
            print(f"Name has been changed to {firstName} {lastName}.")
        case 2:
            print("RANDOM NICKNAME")
            print(f"{firstName} \"{nicknames[random.randint(0, len(nicknames))]}\" {lastName}")
        case 3:
            print("ALL NICKNAMES")
            for i in range(0, len(arr)):
                print(f"{firstName} \"{nicknames[i]}\" {lastName}")
        case 4:
            print("ADD A NICKNAME")
            nickname = input("Please enter a nickname to add: ")
            if nickname in nicknames:
                print(f"{nickname} is already in the nickname list.")
            else:
                nicknames.append(nickname)
                print(f"{nickname} added to the list.")
        case 5:
            print("REMOVE A NICKNAME")