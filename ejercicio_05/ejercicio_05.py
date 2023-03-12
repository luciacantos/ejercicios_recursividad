'''
Ejercicio 5: Búsqueda por dicotomía en una tabla ordenada
'''
def búsqueda_dictómica(elemento, tabla, índice_min, índice_max):


    if tabla[índice_min(tabla)] <= elemento <= tabla[índice_max(tabla)]:
        if elemento < tabla[índice_min(tabla)] or elemento > tabla[índice_max(tabla)]:
            return "Vacío"
        else:
            return búsqueda_dictómica_recursiva(elemento, tabla)
    else:
        return "Tabla no ordenada correctamente"


def búsqueda_dictómica_recursiva(elemento, tabla_ordenada):
    len = len(tabla_ordenada)
    n = len / 2

    if tabla_ordenada[n] == elemento:
        return n
    elif tabla_ordenada[n] > elemento:
        return búsqueda_dictómica_recursiva(elemento, tabla_ordenada[1:n-1])
    else:
        return búsqueda_dictómica_recursiva(elemento, tabla_ordenada[n+1:len])
