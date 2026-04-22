from tracking import trackingLoop
from projects import projectsLoop
from finance import financeLoop


def mainMenu():
    """
    Muestra el menú principal de la aplicación y captura la elección del usuario.
    
    Retorna:
        str: La opción ingresada por el usuario.
    """
    #imprime el encabezado del programa
    print("== FREELANCE HUB ==")

    # Imprime las opciones disponibles del menú
    print("1. Projects")
    print("2. Time tracking")
    print("3. Finances")
    print("4. Tasks")
    print("5. Exit")

    # Captura y retorna la entrada del usuario
    choice = input("Choose an option: ")
    return choice


def apploop():
    """
    Bucle principal de la aplicación que mantiene el programa en ejecución
    hasta que el usuario decide salir.
    Muestra continuamente el menú principal y ejecuta la acción
    correspondiente a la opción elegida. Si se ingresa una opción inválida,
    notifica al usuario y vuelve a mostrar el menú.
    """
    while True:
        # Obtiene la opción seleccionada por el usuario
        choice = mainMenu()
        # Redirige al módulo correspondiente según la opción elegida
        if choice == "1":
            projectsLoop()
        elif choice == "2":
            trackingLoop()
        elif choice == "3":
            financeLoop()
        elif choice == "4":
            print("Tasks") # TODO: llamar al módulo de finanzas
        elif choice == "5":
            print("Goodbye") # Sale del bucle y termina el programa
            break
        else:
            # Notifica al usuario si la opción ingresada no es válida
            print("The chosen option is invalid")
            
if __name__ == "__main__": # Punto de entrada: evita que el programa se ejecute automáticamente al ser importado por otro módulo
    apploop()

    


