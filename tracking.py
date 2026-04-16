import time

def startSession(projectId):
    """
    Captura el datetime actual para marcar inicio de trabajo en un proyecto.

    - input: projectId, Int

    - output: Float
    """
    return time.time() # TODO: Logica de diccionarios

def endSession(projectId, startTimestamp):
    """
    Captura datetime de fin, calcular diferencia con el inicio y retornar horas trabajadas.

    - input: projectId, Float
    - input: startTimestamp, Float

    - output: Float
    """

    # TODO: Falta toda la logica de guardado y diccionario

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