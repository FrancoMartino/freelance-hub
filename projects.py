import os

from tables import printTable


projectsData = {}


def isValidNumber(text):
    """
    Verifica si un texto representa un numero positivo o negativo simple.

    - input: text, Str

    - output: Bool
    """
    text = text.strip()

    if text.startswith("-"):
        text = text[1:]

    if text == "":
        return False

    dots = 0
    for char in text:
        if char == ".":
            dots = dots + 1
            if dots > 1:
                return False
        elif not ("0" <= char <= "9"):
            return False

    return True


def isValidFolderName(text):
    """
    Verifica que un texto pueda usarse como nombre de carpeta en Windows.

    - input: text, Str

    - output: Bool
    """
    if text == "" or text == "." or text == "..":
        return False

    invalidChars = '<>:"/\\|?*'
    for char in text:
        if char in invalidChars:
            return False

    return True


def createProject(projectId, projectName, hourlyRate):
    """
    Crea un proyecto en memoria con su precio por hora.

    - input: projectId, Str
    - input: projectName, Str
    - input: hourlyRate, Float

    - output: Tuple[Bool, Str]
    """
    projectId = projectId.strip()
    projectName = projectName.strip()

    if not projectId:
        return False, "El ID del proyecto no puede estar vacio"

    if not projectName:
        return False, "El nombre del proyecto no puede estar vacio"

    if projectId in projectsData:
        return False, "Ya existe un proyecto con ese ID"

    if not isValidFolderName(projectId):
        return False, "El ID del proyecto no puede contener caracteres invalidos para carpeta"

    if not isValidNumber(hourlyRate):
        return False, "La tarifa por hora debe ser un numero"

    rate = float(hourlyRate)

    if rate < 0:
        return False, "La tarifa por hora no puede ser negativa"

    projectsFolder = "proyectos"
    if not os.path.exists(projectsFolder):
        os.mkdir(projectsFolder)

    projectFolder = os.path.join(projectsFolder, projectId)
    if os.path.exists(projectFolder):
        return False, "Ya existe una carpeta para ese ID de proyecto"

    os.mkdir(projectFolder)
    os.mkdir(os.path.join(projectFolder, "docs"))
    os.mkdir(os.path.join(projectFolder, "assets"))
    os.mkdir(os.path.join(projectFolder, "src"))

    projectsData[projectId] = {
        "name": projectName,
        "hourlyRate": rate,
        "folder": projectFolder,
    }
    return True, "Proyecto creado correctamente y carpeta generada"


def getProjectIds():
    """
    Retorna IDs de proyectos ordenados alfabeticamente.

    - output: List[Str]
    """
    return sorted(projectsData.keys())


def getProjectData(projectId):
    """
    Retorna los datos de un proyecto por su ID.

    - input: projectId, Str

    - output: Dict | None
    """
    return projectsData.get(projectId)


def listProjects():
    """
    Muestra todos los proyectos registrados.
    """
    projectIds = getProjectIds()
    if not projectIds:
        print("Todavia no hay proyectos creados")
        return

    rows = []
    for projectId in projectIds:
        data = getProjectData(projectId)
        rows.append([projectId, data["name"], data["hourlyRate"]])

    printTable(["ID Proyecto", "Nombre", "Tarifa por hora"], rows)
    input("Presiona Enter para continuar")


def projectsMenu():
    """
    Muestra las opciones del submodulo de proyectos.

    - output: Str
    """
    os.system("cls")
    print("== PROYECTOS ==")
    print("1. Crear proyecto")
    print("2. Mostrar proyectos")
    print("3. Volver al menu principal")
    return input("Elegi una opcion: ").strip()


def projectsLoop():
    """
    Bucle interactivo del modulo de proyectos.
    """
    while True:
        choice = projectsMenu()

        if choice == "1":
            projectId = input("ID del proyecto: ").strip()
            projectName = input("Nombre del proyecto: ").strip()
            hourlyRate = input("Tarifa por hora: ").strip()

            created, message = createProject(projectId, projectName, hourlyRate)
            print(message)

        elif choice == "2":
            listProjects()

        elif choice == "3":
            print("Volviendo al menu principal")
            break

        else:
            print("La opcion elegida no es valida")