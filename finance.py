from projects import getProjectData, getProjectIds


def trimSpaces(text):
    """
    Quita espacios al inicio y al final de un texto.

    - input: text, Str

    - output: Str
    """
    while text.startswith(" "):
        text = text[1:]

    while text.endswith(" "):
        text = text[:-1]

    return text


def isValidNumber(text):
    """
    Verifica si un texto representa un numero positivo o negativo simple.

    - input: text, Str

    - output: Bool
    """
    text = trimSpaces(text)

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


def calculateBudget(estimatedHours, hourlyRate):
    """
    Calcula el costo total de un proyecto.

    - input: estimatedHours, Float
    - input: hourlyRate, Float

    - output: Float
    """
    hours = float(estimatedHours)
    rate = float(hourlyRate)

    totalCost = hours * rate
    return totalCost


def convertCurrency(amountArs, currency):
    """
    Convierte un monto de ARS a la moneda seleccionada.

    - input: amountArs, Float
    - input: currency, Str

    - output: Float | None
    """
    exchangeRates = {
        'USD': 1500,
        'EUR': 1600,
        'BRL': 300,
    }

    currency = currency.upper()

    if currency not in exchangeRates:
        print("Error. Moneda no soportada. Monedas disponibles: USD, EUR, BRL.")
        return None

    converted = float(amountArs) / exchangeRates[currency]
    return converted


def financeMenu():
    """
    Muestra las opciones del submodulo de finanzas.

    - output: Str
    """
    print("\n== FINANZAS ==")
    print("1. Calcular presupuesto personalizado")
    print("2. Calcular presupuesto por proyecto")
    print("3. Convertir moneda desde ARS")
    print("4. Volver al menu principal")
    return trimSpaces(input("Elegi una opcion: "))


def showProjectOptions(projectIds):
    """
    Muestra proyectos numerados desde 1.

    - input: projectIds, List[Str]
    """
    index = 1
    for projectId in projectIds:
        data = getProjectData(projectId)
        print(str(index) + ". " + projectId + " (tarifa: " + str(data["hourlyRate"]) + ")")
        index = index + 1


def chooseProjectForBudget():
    """
    Permite elegir un proyecto para calcular presupuesto.

    - output: Str | None
    """
    projectIds = getProjectIds()
    if not projectIds:
        return None

    showProjectOptions(projectIds)
    selected = trimSpaces(input("Selecciona el numero de proyecto: "))

    if not isPositiveInteger(selected):
        print("Por favor, ingresa un numero valido")
        return None

    selectedNumber = int(selected)
    if selectedNumber < 1 or selectedNumber > len(projectIds):
        print("El numero elegido esta fuera de rango")
        return None

    return projectIds[selectedNumber - 1]


def financeLoop():
    """
    Bucle interactivo del modulo de finanzas.
    """
    while True:
        choice = financeMenu()

        if choice == "1":
            estimatedHours = trimSpaces(input("Horas estimadas: "))
            hourlyRate = trimSpaces(input("Tarifa por hora: "))

            if not isValidNumber(estimatedHours) or not isValidNumber(hourlyRate):
                print("Las horas y la tarifa deben ser numeros validos")
                continue

            totalCost = calculateBudget(estimatedHours, hourlyRate)
            print("Presupuesto estimado: " + str(totalCost))

        elif choice == "2":
            projectId = chooseProjectForBudget()
            if projectId is None:
                if not getProjectIds():
                    print("No hay proyectos disponibles. Crea uno en el modulo Proyectos")
                continue

            data = getProjectData(projectId)
            estimatedHours = trimSpaces(input("Horas estimadas para " + projectId + ": "))

            if not isValidNumber(estimatedHours):
                print("Las horas estimadas deben ser un numero valido")
                continue

            totalCost = calculateBudget(estimatedHours, data["hourlyRate"])
            print("Proyecto: " + projectId)
            print("Tarifa por hora: " + str(data["hourlyRate"]))
            print("Presupuesto estimado: " + str(totalCost))

        elif choice == "3":
            amountArs = trimSpaces(input("Monto en ARS: "))
            currency = trimSpaces(input("Moneda destino (USD/EUR/BRL): "))

            if not isValidNumber(amountArs):
                print("El monto debe ser un numero valido")
                continue

            converted = convertCurrency(amountArs, currency)

            if converted is not None:
                print("Monto convertido: " + str(converted) + " " + currency.upper())

        elif choice == "4":
            print("Volviendo al menu principal")
            break

        else:
            print("La opcion elegida no es valida")




