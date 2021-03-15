def main():
    print("""
**************************************************
1) Edit teams
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
