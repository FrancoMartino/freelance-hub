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
    print("2. Tasks")
    print("3. Time Tracking")
    print("4. Finances")
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
            print("projects")  #TODO: llamar al modulo de proyectos
        elif choice == "2":
            print("Tasks") # TODO: llamar al módulo de tareas
        elif choice == "3":
            print("Time Tracking") #TODO: llamar al modulo de seguimiento de tiempo
        elif choice == "4":
            print("Finances") # TODO: llamar al módulo de finanzas
        elif choice == "5":
            print("Goodbye") # Sale del bucle y termina el programa
            break
        else:
            # Notifica al usuario si la opción ingresada no es válida
            print("The chosen option is invalid")
            
if __name__ == "__main__": # Punto de entrada: evita que el programa se ejecute automáticamente al ser importado por otro módulo
    apploop()

    


