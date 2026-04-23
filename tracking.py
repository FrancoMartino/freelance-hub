import os
import time
from projects import getProjectIds
from tables import printTable

# Estado en memoria para la ejecucion actual del programa.
active_sessions = {}
project_hours = {}


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
    makeRow = lambda p_id, hrs: [p_id, formatDuration(hrs)]

    reportMatrix = [["ID Proyecto", "Duracion total"]]
    for p_id, hrs in allData.items():
        reportMatrix.append(makeRow(p_id, hrs))

    return reportMatrix


def trackingMenu():
    """
    Muestra las opciones del submodulo de seguimiento de tiempo.

    - output: Str
    """
    os.system("cls")
    print("== SEGUIMIENTO DE TIEMPO ==")
    print("1. Iniciar sesion")
    print("2. Finalizar sesion")
    print("3. Mostrar reporte")
    print("4. Volver al menu principal")
    return input("Elegi una opcion: ").strip()


def printReportMatrix(reportMatrix):
    """
    Imprime una matriz en formato de tabla simple para consola.

    - input: reportMatrix, List[List]
    """
    if not reportMatrix:
        return

    headers = reportMatrix[0]
    rows = reportMatrix[1:]
    printTable(headers, rows)
    input("Presiona Enter para continuar")


def pauseToContinue():
    input("Presiona Enter para continuar")


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

        selected = input("Selecciona el numero de proyecto: ").strip()
        if not isPositiveInteger(selected):
            print("Por favor, ingresa un numero valido")
            continue

        selectedNumber = int(selected)

        if 1 <= selectedNumber <= len(projects):
            return projects[selectedNumber - 1]

        print("El numero elegido esta fuera de rango")


def pickOrCreateProject():
    """
    Permite elegir un proyecto existente por numero.
    Si no hay proyectos, retorna None.

    - output: Str | None
    """
    knownProjects = getKnownProjects()

    if not knownProjects:
        return None

    print("\nProyectos disponibles:")
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
    return str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)


def trackingLoop():
    """
    Bucle interactivo del modulo de time tracking.
    """
    while True:
        choice = trackingMenu()

        if choice == "1":
            projectId = pickOrCreateProject()

            if projectId is None:
                print("No hay proyectos disponibles. Crea uno en el modulo Proyectos")
                pauseToContinue()
                continue

            if projectId in active_sessions:
                print("Ya hay una sesion activa para ese proyecto")
                pauseToContinue()
                continue

            active_sessions[projectId] = startSession(projectId)
            print(f"Sesion iniciada para el proyecto {projectId}")
            pauseToContinue()

        elif choice == "2":
            activeProjectIds = sorted(active_sessions.keys())
            if not activeProjectIds:
                print("No hay sesiones activas para finalizar")
                pauseToContinue()
                continue

            print("\nSesiones activas:")
            projectId = chooseProjectByNumber(activeProjectIds)
            if projectId is None:
                print("No hay sesiones activas para finalizar")
                pauseToContinue()
                continue

            startTimestamp = active_sessions.pop(projectId)
            sessionNetHours = endSession(projectId, startTimestamp)
            totalHours = project_hours.get(projectId, 0.0)
            project_hours[projectId] = accumulateHours(totalHours, sessionNetHours)

            print(f"Sesion finalizada para el proyecto {projectId}")
            print("Duracion de la sesion: " + formatDuration(sessionNetHours))
            print("Horas de la sesion: " + formatDuration(sessionNetHours))
            print("Horas acumuladas: " + formatDuration(project_hours[projectId]))
            pauseToContinue()

        elif choice == "3":
            if not project_hours:
                print("Todavia no hay tiempo registrado")
                pauseToContinue()
                continue

            report = generateTimeReport(project_hours)
            printReportMatrix(report)

        elif choice == "4":
            print("Volviendo al menu principal")
            break

        else:
            print("La opcion elegida no es valida")