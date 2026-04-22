def repeatChar(charValue, count):
    """
    Repite un caracter una cantidad dada de veces.

    - input: charValue, Str
    - input: count, Int

    - output: Str
    """
    result = ""
    for i in range(count):
        result = result + charValue
    return result


def padRight(textValue, totalWidth):
    """
    Completa un texto con espacios a la derecha hasta un ancho fijo.

    - input: textValue, Str
    - input: totalWidth, Int

    - output: Str
    """
    textValue = str(textValue)
    while len(textValue) < totalWidth:
        textValue = textValue + " "
    return textValue


def normalizeRows(headers, rows):
    """
    Normaliza las filas para que tengan la misma cantidad de columnas que los encabezados.

    - input: headers, List[Str]
    - input: rows, List[List]

    - output: List[List[Str]]
    """
    normalizedRows = []
    for row in rows:
        normalizedRow = []
        for index in range(len(headers)):
            if index < len(row):
                normalizedRow.append(str(row[index]))
            else:
                normalizedRow.append("")
        normalizedRows.append(normalizedRow)
    return normalizedRows


def calculateColumnWidths(headers, rows):
    """
    Calcula el ancho necesario para cada columna de una tabla.

    - input: headers, List[Str]
    - input: rows, List[List[Str]]

    - output: List[Int]
    """
    widths = []
    for header in headers:
        widths.append(len(str(header)))

    for row in rows:
        for index in range(len(headers)):
            cellWidth = len(str(row[index]))
            if cellWidth > widths[index]:
                widths[index] = cellWidth

    return widths


def buildSeparator(widths):
    """
    Construye la linea separadora superior e inferior de una tabla.

    - input: widths, List[Int]

    - output: Str
    """
    separator = "+"
    for width in widths:
        separator = separator + repeatChar("-", width + 2) + "+"
    return separator


def buildRow(values, widths):
    """
    Construye una fila de tabla con sus celdas alineadas.

    - input: values, List[Str]
    - input: widths, List[Int]

    - output: Str
    """
    rowText = "|"
    for index in range(len(widths)):
        rowText = rowText + " " + padRight(values[index], widths[index]) + " |"
    return rowText


def printTable(headers, rows):
    """
    Imprime una tabla simple y reutilizable para consola.

    - input: headers, List[Str]
    - input: rows, List[List]
    """
    normalizedRows = normalizeRows(headers, rows)
    widths = calculateColumnWidths(headers, normalizedRows)

    separator = buildSeparator(widths)
    print(separator)
    print(buildRow(headers, widths))
    print(separator)

    for row in normalizedRows:
        print(buildRow(row, widths))

    print(separator)