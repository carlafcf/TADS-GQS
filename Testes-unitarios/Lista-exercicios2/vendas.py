def percentual_vendas(lista):
    total_produtos = 0
    produtos_id = []
    produtos_qnt = []
    resultado = []

    for produto in lista:
        if produto[1] not in produtos_id:
            produtos_id.append(produto[1])
            produtos_qnt.append(produto[2])
        else:
            indice = produtos_id.index(produto[1])
            produtos_qnt[indice] += produto[2]
        total_produtos += produto[2]

    i = 0
    for produto in produtos_id:
        perc = round(produtos_qnt[i]/total_produtos, 4)
        perc_produto = [produto, perc]
        resultado.append(perc_produto)
        i += 1

    return resultado

def total_vendas(lista):
    total = 0
    for venda in lista:
        total += venda[1]
    return total

def melhoria_vendas(parametro, lista):
    i=0
    for mes in lista:
        if parametro == mes[0]:
            break
        i += 1

    if i == 0:
        return False
    else:
        valor_atual = lista[i][1]
        valor_anterior = lista[i-1][1]
        return round((valor_atual-valor_anterior)/valor_anterior, 4)