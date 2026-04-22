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




