def mainMenu():
    print("== FREELANCE HUB ==")
    print("1. Projects")
    print("2. Tasks")
    print("3. Time Tracking")
    print("4. Finances")
    print("5. Exit")

    choice = input("Choose an option: ")
    return choice


def apploop():
    while True:
        choice = mainMenu()
        if choice == "1":
            print("projects")
        elif choice == "2":
            print("Tasks")
        elif choice == "3":
            print("Time Tracking")
        elif choice == "4":
            print("Finances")
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("The chosen option is invalid")
            
if __name__ == "__main__": #Prevents the program from running automatically when imported by another module.
    apploop()

    


