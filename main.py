from tracking import trackingLoop
from projects import projectsLoop
from finance import financeLoop


def mainMenu():
    """
    Muestra el menú principal de la aplicación y captura la elección del usuario.

    - output: Str
    """
    print("== FREELANCE HUB ==")
    print("1. Projects")
    print("2. Time tracking")
    print("3. Finances")
    print("4. Tasks")
    print("5. Exit")

    choice = input("Choose an option: ")
    return choice


def appLoop():
    """
    Bucle principal de la aplicación que mantiene el programa en ejecución
    hasta que el usuario decide salir.
    """
    while True:
        choice = mainMenu()

        if choice == "1":
            projectsLoop()
        elif choice == "2":
            trackingLoop()
        elif choice == "3":
            financeLoop()
        elif choice == "4":
            print("Tasks module coming soon")
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("The chosen option is invalid")


if __name__ == "__main__":
    appLoop()

    


