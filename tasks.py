tasksData = {}
nextTaskId = 1


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


def repeatChar(charValue, count):
    """
    Repite un caracter una cantidad dada de veces.

    - input: charValue, Str
    - input: count, Int

    - output: Str
    """
    result = ""
    for _ in range(count):
        result = result + charValue
    return result


def padRight(textValue, totalWidth):
    """
    Completa un texto con espacios a la derecha hasta un ancho fijo.

    - input: textValue, Str
    - input: totalWidth, Int

    - output: Str
    """
    textValue = str(textValue)
    while len(textValue) < totalWidth:
        textValue = textValue + " "
    return textValue


def printTasksHeader(idWidth, statusWidth, descriptionWidth):
    """
    Imprime encabezado y separadores de la tabla de tareas.

    - input: idWidth, Int
    - input: statusWidth, Int
    - input: descriptionWidth, Int
    """
    separator = "+" + repeatChar("-", idWidth + 2) + "+" + repeatChar("-", statusWidth + 2) + "+" + repeatChar("-", descriptionWidth + 2) + "+"
    titleRow = "| " + padRight("ID", idWidth) + " | " + padRight("Estado", statusWidth) + " | " + padRight("Descripcion", descriptionWidth) + " |"

    print(separator)
    print(titleRow)
    print(separator)


def listTasks():
    """
    Muestra todas las tareas registradas.
    """
    taskIds = getTaskIds()
    if not taskIds:
        print("No hay tareas cargadas")
        return

    idWidth = len("ID")
    statusWidth = len("Estado")
    descriptionWidth = len("Descripcion")

    for taskId in taskIds:
        taskData = tasksData[taskId]
        status = "Hecha" if taskData["done"] else "Pendiente"

        if len(str(taskId)) > idWidth:
            idWidth = len(str(taskId))

        if len(status) > statusWidth:
            statusWidth = len(status)

        if len(taskData["description"]) > descriptionWidth:
            descriptionWidth = len(taskData["description"])

    printTasksHeader(idWidth, statusWidth, descriptionWidth)

    for taskId in taskIds:
        taskData = tasksData[taskId]
        status = "Hecha" if taskData["done"] else "Pendiente"
        row = "| " + padRight(taskId, idWidth) + " | " + padRight(status, statusWidth) + " | " + padRight(taskData["description"], descriptionWidth) + " |"
        print(row)

    separator = "+" + repeatChar("-", idWidth + 2) + "+" + repeatChar("-", statusWidth + 2) + "+" + repeatChar("-", descriptionWidth + 2) + "+"
    print(separator)


def chooseTaskId():
    """
    Permite elegir una tarea por su ID.

    - output: Int | None
    """
    if not tasksData:
        return None

    selected = input("Ingresa el ID de la tarea: ").strip()
    if not selected.isdigit():
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
    print("\n== TAREAS ==")
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
