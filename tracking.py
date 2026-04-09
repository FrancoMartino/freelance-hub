import time

def startSession(projectId):
    """
    Captura el datetime actual para marcar inicio de trabajo en un proyecto.

    - input: projectId, Int

    - output: Float
    """
    return time.time()

def endSession(startTimestamp):
    """
    Captura datetime de fin, calcular diferencia con el inicio y retornar horas trabajadas.

    - input: startTimestamp, Float

    - output: Float
    """
    calcHours = lambda start, end: round((end - start) / 3600, 4)
    return calcHours(startTimestamp, time.time())