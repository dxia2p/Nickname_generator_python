import random

firstName = input("Enter your first name") # input for user's name
lastName = input("Enter your last name")
nicknames = ["The Bulldog", "Crusher", "The Scientist", "Twinkle-toes", "the Coder"] # array with all nicknames

def DisplayMenu(): # function that displays the menu
    print(f"MAIN MENU ({firstName} {lastName})")
    print("1. Change Name")
    print("2. Display a Random Nickname")
    print("3. Display all Nicknames")
    print("4. Add a Nickname")
    print("5. Remove a Nickname")
    print("6. Exit")
    return int(input("Enter #"))

inp = DisplayMenu()
while inp != 6: # keep looping until the user presses 6
    match inp:
        case 1: # change name
            print("CHANGE NAME")
            firstName = input("Enter your first name")
            lastName = input("Enter your last name")
            print(f"Name has been changed to {firstName} {lastName}.")
        case 2: # display a random nickname from the list of nicknames
            print("RANDOM NICKNAME")
            print(f"{firstName} \"{nicknames[random.randint(0, len(nicknames) - 1)]}\" {lastName}")
        case 3: # display all nicknames
            print("ALL NICKNAMES")
            for i in range(0, len(nicknames)):
                print(f"{firstName} \"{nicknames[i]}\" {lastName}")
        case 4: # ask user to add a nickname and if it already exists don't add it
            print("ADD A NICKNAME")
            nickname = input("Please enter a nickname to add: ")
            if nickname in nicknames:
                print(f"{nickname} is already in the nickname list.")
            else:
                nicknames.append(nickname)
                print(f"{nickname} added to the list.")
        case 5: # ask user to remove an nickname and if it does not exist do not remove it
            print("REMOVE A NICKNAME")
            nickname = input("Please enter a nickname to remove: ")
            if nickname in nicknames:
                nicknames.remove(nickname)
                print(f"{nickname} removed from the nickname list.")
            else:
                print(f"{nickname} was not found in the nickname list.")
    inp = DisplayMenu()