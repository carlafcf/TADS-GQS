from produto import Produto
from usuario import Usuario

class Venda:

    def __init__(self):
        self.produtos = []

    def inserirProduto(self, produto, quantidade):
        if (produto.getEstoque() >= quantidade):
            self.produtos.append([produto, quantidade])
            produto.setEstoque(produto.getEstoque() - quantidade)
        else:
            print("Produto " + produto.nome + " não tem quantidade suficiente e foi removido do carrinho de compras.")

    def setUsuario(self, usuario):
        self.usuario = usuario

    def getUsuario(self):
        return self.usuario

    def getProdutos(self):
        return self.produtos

