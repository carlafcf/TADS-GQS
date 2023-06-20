from django.test import TestCase
from unittest.mock import Mock

from Produto.models import Produto


class ProdutoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Produto.objects.create(nome="Travesseiro", fornecedor="Forn. 3", qnt_em_estoque=100, preco_de_venda=30.10)
        Produto.objects.create(nome="Travesseiro", fornecedor="Forn. 2", qnt_em_estoque=10, preco_de_venda=29.99)
        Produto.objects.create(nome="Cama", fornecedor="Forn. 1", qnt_em_estoque=50, preco_de_venda=200.50)
        Produto.objects.create(nome="Lençol", fornecedor="Forn. 2", qnt_em_estoque=3, preco_de_venda=50.99)

    def test_ordering(self):
        lista_ordenada = [Produto.objects.get(id=3), Produto.objects.get(id=4),
                          Produto.objects.get(id=2), Produto.objects.get(id=1)]
        # lista_ordenada = Produtos.objects.all().order_by('nome', 'fornecedor')
        # produtos = list(Produtos.objects.all())
        produtos = [entry for entry in Produto.objects.all()]
        self.assertEquals(lista_ordenada, produtos)

    def test_nome_label(self):
        produto = Produto.objects.get(id=1)
        label_do_produto = produto._meta.get_field('nome').verbose_name
        self.assertEquals(label_do_produto, "Nome")

    def test_fornecedor_label(self):
        produto = Produto.objects.get(id=1)
        label_do_produto = produto._meta.get_field('fornecedor').verbose_name
        self.assertTrue(label_do_produto == "Fornecedor")

    def test_qnt_em_estoque_label(self):
        produto = Produto.objects.get(id=1)
        label_do_produto = produto._meta.get_field('qnt_em_estoque').verbose_name
        self.assertEquals(label_do_produto, "Quantidade em estoque")

    def test_preco_de_venda_label(self):
        produto = Produto.objects.get(id=1)
        label_do_produto = produto._meta.get_field('preco_de_venda').verbose_name
        self.assertEquals(label_do_produto, "Preço de venda")

    def test_nome_max_length(self):
        produto = Produto.objects.get(id=1)
        max_length = produto._meta.get_field('nome').max_length
        self.assertEquals(max_length, 200)

    def test_fornecedor_max_length(self):
        produto = Produto.objects.get(id=1)
        max_length = produto._meta.get_field('fornecedor').max_length
        self.assertEquals(max_length, 200)