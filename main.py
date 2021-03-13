# Torment Tracker by Elliott Strutton
from os import system, name
from time import sleep

ver = "1.1.0"

teamOne = {}
teamTwo = {}
teamThree = {}
TeamFour = {}
Solos = {}

eventOneParticipants = {}
eventTwoParticipants = {}
eventThreeParticipants = {}
eventFourParticipants = {}
eventFiveParticipants = {}


def main():
    # Selection menu
    print("""
**************************************************
1) Edit teams and participants list
2) Edit tournament names
3) Edit scores
4) Calculate scores
5) Exit
**************************************************    
""")
    selection = input(">")
    if selection == "1":
        new_participants()
    elif selection == "2":
        print("2")
    elif selection == "3":
        print("3")
    elif selection == "4":
        print("4")
    elif selection == "5":
        print("5")
    else:
        # Help Message
        print("\n \n \nPlease enter a number that corresponds with the menu options")
        main()


def new_participants():
    print("""
**************************************************
1) Add team
2) Add participants to team
3) Remove participants from team
4) Add solo participants
5) Remove solo participants
6) Back to main menu
**************************************************    
""")
    selection = input(">")
    if selection == "1":
        print("1")
    elif selection == "2":
        print("2")
    elif selection == "3":
        print("3")
    elif selection == "4":
        print("4")
    elif selection == "5":
        print("5")
    elif selection == "6":
        print("6")
    else:
        # Help Message
        print("\n \n \nPlease enter a number that corresponds with the menu options")
        main()


print("Tournament Tracker")
print("Version :", ver)
main()
