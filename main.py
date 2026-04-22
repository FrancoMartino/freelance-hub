from tracking import trackingLoop
from projects import projectsLoop
from finance import financeLoop
from tasks import tasksLoop


def mainMenu():
    """
    Muestra el menú principal de la aplicación y captura la elección del usuario.

    - output: Str
    """
    print("== FREELANCE HUB ==")
    print("1. Proyectos")
    print("2. Seguimiento de tiempo")
    print("3. Finanzas")
    print("4. Tareas")
    print("5. Salir")

    choice = input("Elegi una opcion: ")
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
            tasksLoop()
        elif choice == "5":
            print("Hasta luego")
            break
        else:
            print("La opcion elegida no es valida")

appLoop()