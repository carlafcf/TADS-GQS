def pacientes_mais_visitas(lista, medico):
    retorno = []
    lista_pacientes = []
    qnt_visitas = []
    for elemento in lista:
        if elemento[3] == medico:

            # Encontrar os pacientes desse médico
            if elemento[1] not in lista_pacientes:
                lista_pacientes.append(elemento[1])
                qnt_visitas.append(1)
            else:
                indice = lista_pacientes.index(elemento[1])
                qnt_visitas[indice] = qnt_visitas[indice] + 1

    if (len(lista_pacientes) > 0):
        maior_valor = max(qnt_visitas)

    for indice, elemento in enumerate(lista_pacientes):
        if qnt_visitas[indice] == maior_valor:
            retorno.append(elemento)

    return retorno

def pacientes_premiados(lista):
    retorno = []
    lista_pacientes = []
    qnt_visitas = []

    for elemento in lista:
        if elemento[1] not in lista_pacientes:
            lista_pacientes.append(elemento[1])
            qnt_visitas.append(1)
        else:
            indice = lista_pacientes.index(elemento[1])
            qnt_visitas[indice] = qnt_visitas[indice] + 1

    for indice, elemento in enumerate(lista_pacientes):
        if qnt_visitas[indice] >= 6:
            retorno.append(elemento)

    return retorno
