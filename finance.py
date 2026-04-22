from projects import getProjectData, getProjectIds


def calculateBudget(estimatedHours, hourlyRate):
    """
    Calcula el costo total de un proyecto.

    Args:
        estimatedHours: cantidad de horas estimadas para el proyecto.
        hourlyRate: precio por hora.

    Returns:
        totalCost: costo total del proyecto.
    """
    hours = float(estimatedHours)
    rate = float(hourlyRate)

    totalCost = hours * rate
    return totalCost


def convertCurrency(amountArs, currency):
    """
    Convierte un monto de ARS a la moneda seleccionada.

    Args:
        amountArs: monto en pesos argentinos.
        currency: monedas ('USD', 'EUR', 'BRL').

    Returns:
        converted: devuelve el monto convertido, o None si la moneda no es soportada.
    """
    exchangeRates = {
        'USD': 1500,
        'EUR': 1600,
        'BRL': 300,
    }

    currency = currency.upper()

    if currency not in exchangeRates:
        print("Error. Unsoported currency. Supported currencies are: USD, EUR, BRL.")
        return None

    converted = float(amountArs) / exchangeRates[currency]
    return converted


def financeMenu():
    """
    Muestra las opciones del submodulo de finanzas.

    - output: Str
    """
    print("\n== FINANCES ==")
    print("1. Calculate custom budget")
    print("2. Calculate budget by project")
    print("3. Convert ARS currency")
    print("4. Back to main menu")
    return input("Choose an option: ").strip()


def showProjectOptions(projectIds):
    """
    Muestra proyectos numerados desde 1.

    - input: projectIds, List[Str]
    """
    index = 1
    for projectId in projectIds:
        data = getProjectData(projectId)
        print(str(index) + ". " + projectId + " (rate: " + str(data["hourlyRate"]) + ")")
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
    selected = input("Select project number: ").strip()

    if not selected.isdigit():
        print("Please enter a valid number")
        return None

    selectedNumber = int(selected)
    if selectedNumber < 1 or selectedNumber > len(projectIds):
        print("The selected number is out of range")
        return None

    return projectIds[selectedNumber - 1]


def financeLoop():
    """
    Bucle interactivo del modulo de finanzas.
    """
    while True:
        choice = financeMenu()

        if choice == "1":
            estimatedHours = input("Estimated hours: ").strip()
            hourlyRate = input("Hourly rate: ").strip()

            try:
                totalCost = calculateBudget(estimatedHours, hourlyRate)
                print("Estimated budget: " + str(totalCost))
            except ValueError:
                print("Hours and rate must be valid numbers")

        elif choice == "2":
            projectId = chooseProjectForBudget()
            if projectId is None:
                if not getProjectIds():
                    print("No projects available. Create one in Projects module")
                continue

            data = getProjectData(projectId)
            estimatedHours = input("Estimated hours for " + projectId + ": ").strip()

            try:
                totalCost = calculateBudget(estimatedHours, data["hourlyRate"])
                print("Project: " + projectId)
                print("Hourly rate: " + str(data["hourlyRate"]))
                print("Estimated budget: " + str(totalCost))
            except ValueError:
                print("Estimated hours must be a valid number")

        elif choice == "3":
            amountArs = input("Amount in ARS: ").strip()
            currency = input("Target currency (USD/EUR/BRL): ").strip()

            try:
                converted = convertCurrency(amountArs, currency)
            except ValueError:
                print("Amount must be a valid number")
                continue

            if converted is not None:
                print("Converted amount: " + str(converted) + " " + currency.upper())

        elif choice == "4":
            print("Returning to main menu")
            break

        else:
            print("The chosen option is invalid")




