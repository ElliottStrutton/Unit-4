# Torment Tracker by Elliott Strutton
from new_participants import main as new_participants


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
2) Edit tournament events
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


print("Tournament Tracker")
print("Version :", ver)
main()
