def max_horas(lista_horas):
    if (len(lista_horas) == 0):
        return []
    resultado = []
    max_horas = lista_horas[0][1]
    for elem in lista_horas:
        if (elem[1] == max_horas):
            resultado.append(elem)
        elif (elem[1] > max_horas):
            max_horas = elem[1]
            resultado = []
            resultado.append(elem)
    return resultado
