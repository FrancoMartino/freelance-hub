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
        return False, "Project ID cannot be empty"

    if not projectName:
        return False, "Project name cannot be empty"

    if projectId in projectsData:
        return False, "A project with that ID already exists"

    try:
        rate = float(hourlyRate)
    except ValueError:
        return False, "Hourly rate must be a number"

    if rate < 0:
        return False, "Hourly rate cannot be negative"

    projectsData[projectId] = {
        "name": projectName,
        "hourlyRate": rate,
    }
    return True, "Project created successfully"


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
    print("Project ID | Name | Hourly Rate")
    for projectId in projectIds:
        data = getProjectData(projectId)
        print(projectId + " | " + data["name"] + " | " + str(data["hourlyRate"]))


def listProjects():
    """
    Muestra todos los proyectos registrados.
    """
    projectIds = getProjectIds()
    if not projectIds:
        print("No projects created yet")
        return

    printProjectsTable(projectIds)


def projectsMenu():
    """
    Muestra las opciones del submodulo de proyectos.

    - output: Str
    """
    print("\n== PROJECTS ==")
    print("1. Create project")
    print("2. Show projects")
    print("3. Back to main menu")
    return input("Choose an option: ").strip()


def projectsLoop():
    """
    Bucle interactivo del modulo de proyectos.
    """
    while True:
        choice = projectsMenu()

        if choice == "1":
            projectId = input("Project ID: ").strip()
            projectName = input("Project name: ").strip()
            hourlyRate = input("Hourly rate: ").strip()

            created, message = createProject(projectId, projectName, hourlyRate)
            print(message)

        elif choice == "2":
            listProjects()

        elif choice == "3":
            print("Returning to main menu")
            break

        else:
            print("The chosen option is invalid")