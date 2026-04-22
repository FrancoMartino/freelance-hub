projectsData = {}


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

    try:
        rate = float(hourlyRate)
    except ValueError:
        return False, "La tarifa por hora debe ser un numero"

    if rate < 0:
        return False, "La tarifa por hora no puede ser negativa"

    projectsData[projectId] = {
        "name": projectName,
        "hourlyRate": rate,
    }
    return True, "Proyecto creado correctamente"


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


def printProjectsTable(projectIds):
    """
    Imprime una tabla simple de proyectos.

    - input: projectIds, List[Str]
    """
    print("ID Proyecto | Nombre | Tarifa por hora")
    for projectId in projectIds:
        data = getProjectData(projectId)
        print(projectId + " | " + data["name"] + " | " + str(data["hourlyRate"]))


def listProjects():
    """
    Muestra todos los proyectos registrados.
    """
    projectIds = getProjectIds()
    if not projectIds:
        print("Todavia no hay proyectos creados")
        return

    printProjectsTable(projectIds)


def projectsMenu():
    """
    Muestra las opciones del submodulo de proyectos.

    - output: Str
    """
    print("\n== PROYECTOS ==")
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