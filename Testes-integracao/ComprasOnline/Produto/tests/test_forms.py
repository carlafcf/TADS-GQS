from django.test import TestCase

from Produto.models import Produto
from Produto.forms import ProdutoForm

class ProdutoFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Produto.objects.create(nome="TV", fornecedor="Magazine Luiza", qnt_em_estoque=50, preco_de_venda=1000.00)

    def test_produto_fornecedor_existente(self):
        form = ProdutoForm(data={'nome': 'TV', 'fornecedor': 'Magazine Luiza', 'preco_de_venda':50.50})
        self.assertFalse(form.is_valid())
    
    def test_produto_fornecedor_nao_existente_1(self):
        form = ProdutoForm(data={'nome': 'TV', 'fornecedor': 'Loja das TVs', 'preco_de_venda':50.50})
        self.assertTrue(form.is_valid())

    def test_produto_fornecedor_nao_existente_2(self):
        form = ProdutoForm(data={'nome': 'Computador', 'fornecedor': 'Magazine Luiza', 'preco_de_venda':50.50})
        self.assertTrue(form.is_valid())

    def test_elementos_obrigatorios_1(self):
        form = ProdutoForm(data={'nome': '', 'fornecedor': 'Magazine Luiza', 'preco_de_venda': 100.00})
        self.assertFalse(form.is_valid())

    def test_elementos_obrigatorios_2(self):
        form = ProdutoForm(data={'nome': 'Computador', 'fornecedor': '', 'preco_de_venda': 100.00})
        self.assertFalse(form.is_valid())