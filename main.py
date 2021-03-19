# Torment Tracker by Elliott Strutton
from colorama import Fore, Style
from time import sleep

ver = "1.1.0"

teamOne = {
    "name": "no_name",
    "members": [],
    "score": 0
}
teamTwo = {
    "name": "no_name",
    "members": [],
    "score": 0
}
teamThree = {
    "name": "no_name",
    "members": [],
    "score": 0
}
teamFour = {
    "name": "no_name",
    "members": [],
    "score": 0
}
solos = []

eventOneParticipants = []
eventTwoParticipants = []
eventThreeParticipants = []
eventFourParticipants = []
eventFiveParticipants = []


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
        menuError()
        main()


def new_participants():
    print("""
**************************************************
1) Edit team names
2) Add participants to team
3) Remove participants from team
4) Add solo participants
5) Remove solo participants
6) Back to main menu
**************************************************    
""")
    selection = input(">")
    if selection == "1":
        teamEdit()
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
        menuError()
    new_participants()


def menuError():
    print(f"\n \n \n{Fore.RED}Please enter a number that corresponds with the menu options{Style.RESET_ALL}")


def teamEdit():
    print(f"""
**************************************************
1) Team one ({teamOne["name"]})
2) Team two ({teamTwo["name"]})
3) Team three ({teamThree["name"]})
4) Team four ({teamFour["name"]})
5) Back to team and participant edits 
**************************************************    
            """)
    selection = input(">")
    if selection == "1":
        print("Enter Team ones new name")
        teamOne["name"] = input(">")
        print(f"Team ones new name is {teamOne['name']}")
        sleep(2)
        teamEdit()

    elif selection == "2":
        print("Enter Team twos new name")
        teamTwo["name"] = input(">")
        print(f"Team twos new name is {teamTwo['name']}")
        sleep(2)
        teamEdit()
    elif selection == "3":
        print("Enter Team threes new name")
        teamThree["name"] = input(">")
        print(f"Team threes new name is {teamThree['name']}")
        sleep(2)
        teamEdit()
    elif selection == "4":
        print("Enter Team fours new name")
        teamFour["name"] = input(">")
        print(f"Team fours new name is {teamFour['name']}")
        sleep(2)
        teamEdit()
    elif selection == "5":
        new_participants()
    else:
        # Help Message
        menuError()
        teamEdit()


print("Tournament Tracker")
print("Version :", ver)
sleep(2)
main()
