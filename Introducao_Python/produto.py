class Produto:

    def __init__(self, nome, valor, estoque):
        self.nome = nome
        self.valor = valor
        self.estoque = estoque

    def setNome(self, nome):
        self.nome = nome

    def setValor(self, valor):
        self.valor = valor

    def setEstoque(self, estoque):
        self.estoque = estoque

    def getNome(self):
        return self.nome

    def getValor(self):
        return self.valor

    def getEstoque(self):
        return self.estoque

