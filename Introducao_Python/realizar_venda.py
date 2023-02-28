from venda import Venda
from produto import Produto
from usuario import Usuario

produto1 = Produto("bolacha", 5.5, 10)
produto2 = Produto("chocolate", 7.5, 8)
produto3 = Produto("maçã", 2.99, 40)
produto4 = Produto("ketchup", 11.50, 2)

usuario1 = Usuario("Carla")
usuario2 = Usuario("Danilo")
usuario3 = Usuario("Daniel")
usuario4 = Usuario("Alice")

venda1 = Venda()
venda1.setUsuario(usuario1)
venda1.inserirProduto(produto1, 5)
venda1.inserirProduto(produto2, 10)
venda1.inserirProduto(produto3, 10)
venda1.inserirProduto(produto1, 5)
venda1.inserirProduto(produto1, 2)

for produto in venda1.getProdutos():
    print(produto[0].nome + " " + str(produto[1]))