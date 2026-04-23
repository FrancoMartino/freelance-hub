import os

tasksData = {}
nextTaskId = 1

from tables import printTable


def isPositiveInteger(text):
    """
    Verifica si un texto contiene solo digitos.

    - input: text, Str

    - output: Bool
    """
    if text == "":
        return False

    for char in text:
        if not ("0" <= char <= "9"):
            return False

    return True


def createTask(taskDescription):
    """
    Crea una tarea nueva en memoria.

    - input: taskDescription, Str

    - output: Tuple[Bool, Str]
    """
    global nextTaskId

    taskDescription = taskDescription.strip()
    if not taskDescription:
        return False, "La descripcion de la tarea no puede estar vacia"

    tasksData[nextTaskId] = {
        "description": taskDescription,
        "done": False,
    }
    nextTaskId = nextTaskId + 1
    return True, "Tarea creada correctamente"


def getTaskIds():
    """
    Retorna IDs de tareas ordenados de menor a mayor.

    - output: List[Int]
    """
    return sorted(tasksData.keys())


def listTasks():
    """
    Muestra todas las tareas registradas.
    """
    taskIds = getTaskIds()
    if not taskIds:
        print("No hay tareas cargadas")
        return

    rows = []
    for taskId in taskIds:
        taskData = tasksData[taskId]
        status = "Hecha" if taskData["done"] else "Pendiente"
        rows.append([taskId, status, taskData["description"]])

    printTable(["ID", "Estado", "Descripcion"], rows)
    input("Presiona Enter para continuar")


def chooseTaskId():
    """
    Permite elegir una tarea por su ID.

    - output: Int | None
    """
    if not tasksData:
        return None

    selected = input("Ingresa el ID de la tarea: ").strip()
    if not isPositiveInteger(selected):
        print("Por favor, ingresa un numero valido")
        return None

    taskId = int(selected)
    if taskId not in tasksData:
        print("No existe una tarea con ese ID")
        return None

    return taskId


def markTaskAsDone(taskId):
    """
    Marca una tarea como completada.

    - input: taskId, Int

    - output: Str
    """
    if tasksData[taskId]["done"]:
        return "La tarea ya estaba marcada como hecha"

    tasksData[taskId]["done"] = True
    return "Tarea marcada como hecha"


def deleteTask(taskId):
    """
    Elimina una tarea por ID.

    - input: taskId, Int

    - output: Str
    """
    del tasksData[taskId]
    return "Tarea eliminada"


def tasksMenu():
    """
    Muestra las opciones del submodulo de tareas.

    - output: Str
    """
    os.system("cls")
    print("== TAREAS ==")
    print("1. Crear tarea")
    print("2. Mostrar tareas")
    print("3. Marcar tarea como hecha")
    print("4. Eliminar tarea")
    print("5. Volver al menu principal")
    return input("Elegi una opcion: ").strip()


def tasksLoop():
    """
    Bucle interactivo del modulo de tareas.
    """
    while True:
        choice = tasksMenu()

        if choice == "1":
            taskDescription = input("Descripcion de la tarea: ").strip()
            created, message = createTask(taskDescription)
            print(message)

        elif choice == "2":
            listTasks()

        elif choice == "3":
            if not tasksData:
                print("No hay tareas para marcar")
                continue

            listTasks()
            taskId = chooseTaskId()
            if taskId is None:
                continue

            print(markTaskAsDone(taskId))

        elif choice == "4":
            if not tasksData:
                print("No hay tareas para eliminar")
                continue

            listTasks()
            taskId = chooseTaskId()
            if taskId is None:
                continue

            print(deleteTask(taskId))

        elif choice == "5":
            print("Volviendo al menu principal")
            break

        else:
            print("La opcion elegida no es valida")