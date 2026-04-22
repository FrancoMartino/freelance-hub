import time
from projects import getProjectIds

# Estado en memoria para la ejecucion actual del programa.
active_sessions = {}
project_hours = {}

def startSession(projectId):
    """
    Captura el datetime actual para marcar inicio de trabajo en un proyecto.

    - input: projectId, Str

    - output: Float
    """
    return time.time()

def endSession(projectId, startTimestamp):
    """
    Captura datetime de fin, calcular diferencia con el inicio y retornar horas trabajadas.

    - input: projectId, Str
    - input: startTimestamp, Float

    - output: Float
    """
    calcHours = lambda start, end: round((end - start) / 3600, 4)
    return calcHours(startTimestamp, time.time())

def accumulateHours(projectTotalHours, sessionNetHours):
    """
    Sumar las horas de la sesión actual al total histórico del proyecto en el diccionario.

    - input: projectTotalHours, Float
    - input: sessionNetHours, Float

    - output: Float
    """
    
    return projectTotalHours + sessionNetHours

def generateTimeReport(allData):
    """
    Crear matriz resumen de horas por proyecto para mostrar en consola.

    - input: allData, Dict

    - output: List[List]
    """
    makeRow = lambda p_id, hrs: [p_id, hrs]
    
    reportMatrix = [["Project ID", "Total Hours"]]
    for p_id, hrs in allData.items():
        reportMatrix.append(makeRow(p_id, hrs))
        
    return reportMatrix


def trackingMenu():
    """
    Muestra las opciones del submodulo de seguimiento de tiempo.

    - output: Str
    """
    print("\n== TIME TRACKING ==")
    print("1. Start session")
    print("2. End session")
    print("3. Show report")
    print("4. Back to main menu")
    return input("Choose an option: ").strip()


def printReportMatrix(reportMatrix):
    """
    Imprime una matriz en formato de tabla simple para consola.

    - input: reportMatrix, List[List]
    """
    for row in reportMatrix:
        print(str(row[0]) + " | " + str(row[1]))


def getKnownProjects():
    """
    Retorna lista ordenada de proyectos conocidos por el modulo.
    """
    return sorted(set(getProjectIds()) | set(project_hours.keys()) | set(active_sessions.keys()))


def showProjectsWithNumbers(projects):
    """
    Muestra proyectos numerados desde 1.
    """
    index = 1
    for projectId in projects:
        print(str(index) + ". " + str(projectId))
        index = index + 1


def chooseProjectByNumber(projects):
    """
    Permite elegir proyecto por numero.

    - output: Str | None
    """
    while True:
        if not projects:
            return None

        showProjectsWithNumbers(projects)

        selected = input("Select project number: ").strip()
        if not selected.isdigit():
            print("Please enter a valid number")
            continue

        selectedNumber = int(selected)

        if 1 <= selectedNumber <= len(projects):
            return projects[selectedNumber - 1]

        print("The selected number is out of range")


def pickOrCreateProject():
    """
    Permite elegir un proyecto existente por numero.
    Si no hay proyectos, retorna None.

    - output: Str | None
    """
    knownProjects = getKnownProjects()

    if not knownProjects:
        return None

    print("\nAvailable projects:")
    return chooseProjectByNumber(knownProjects)


def formatDuration(sessionNetHours):
    """
    Convierte horas a formato simple hh:mm:ss.

    - input: sessionNetHours, Float
    - output: Str
    """
    totalSeconds = int(sessionNetHours * 3600)
    hours = totalSeconds // 3600
    minutes = (totalSeconds % 3600) // 60
    seconds = totalSeconds % 60
    return str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s"


def trackingLoop():
    """
    Bucle interactivo del modulo de time tracking.
    """
    while True:
        choice = trackingMenu()

        if choice == "1":
            projectId = pickOrCreateProject()

            if projectId is None:
                print("No projects available. Create one in Projects module")
                continue

            if projectId in active_sessions:
                print("There is already an active session for that project")
                continue

            active_sessions[projectId] = startSession(projectId)
            print(f"Session started for project {projectId}")

        elif choice == "2":
            activeProjectIds = sorted(active_sessions.keys())
            if not activeProjectIds:
                print("No active sessions to finish")
                continue

            print("\nActive sessions:")
            projectId = chooseProjectByNumber(activeProjectIds)
            if projectId is None:
                print("No active sessions to finish")
                continue

            startTimestamp = active_sessions.pop(projectId)
            sessionNetHours = endSession(projectId, startTimestamp)
            totalHours = project_hours.get(projectId, 0.0)
            project_hours[projectId] = accumulateHours(totalHours, sessionNetHours)

            print(f"Session ended for project {projectId}")
            print("Session duration: " + formatDuration(sessionNetHours))
            print(f"Session hours: {sessionNetHours}")
            print(f"Accumulated hours: {project_hours[projectId]}")

        elif choice == "3":
            if not project_hours:
                print("No tracked time yet")
                continue

            report = generateTimeReport(project_hours)
            printReportMatrix(report)

        elif choice == "4":
            print("Returning to main menu")
            break

        else:
            print("The chosen option is invalid")