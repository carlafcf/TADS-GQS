def produtos_reposicao(lista):
    contador = 0
    for produto in lista:
        if (produto[1] < 5):
            contador += 1
    return contador