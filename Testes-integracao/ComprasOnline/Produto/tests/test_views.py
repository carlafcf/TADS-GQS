from django.test import TestCase

from django.urls import reverse

from django.contrib.auth.models import User

from Produto.models import Produto
from Produto import views

import random

class ProdutoViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Produto.objects.create(nome='Produto 1', fornecedor="F", qnt_em_estoque=10, preco_de_venda=200.57, desconto=10.00) #20.057
        Produto.objects.create(nome='Produto 2', fornecedor="F", preco_de_venda=10.50, desconto=5.00) #0.525
        Produto.objects.create(nome='Produto 3', fornecedor="F", qnt_em_estoque=50, preco_de_venda=20.50, desconto=12.00) #2.46
        Produto.objects.create(nome='Produto 4', fornecedor="F", qnt_em_estoque=0, preco_de_venda=200.57, desconto=20.00) #40.114
        Produto.objects.create(nome='Produto 5', fornecedor="F", qnt_em_estoque=2, preco_de_venda=500.50, desconto=55.00) #275.275
    
    def setUp(self):
        usuario = User.objects.create_user(username="testuser", password="123")
        usuario.save()

    def test_listar_produto_url(self):
        response = self.client.get(reverse('produtos:listar_produtos'))
        self.assertEquals(response.status_code, 200)
    
    def test_listar_produto_template(self):
        response = self.client.get(reverse('produtos:listar_produtos'))
        self.assertTemplateUsed(response, 'Produto/listar_produtos.html')

    def test_listar_produto_all(self):
        response = self.client.get(reverse('produtos:listar_produtos'))
        self.assertEquals(len(response.context['lista_produtos']), 5)
    
    def test_listar_produto_em_falta_url(self):
        response = self.client.get(reverse('produtos:listar_produtos_falta'))
        self.assertEquals(response.status_code, 200)
    
    def test_listar_produto_em_falta_template(self):
        response = self.client.get(reverse('produtos:listar_produtos_falta'))
        self.assertTemplateUsed(response, 'Produto/listar_produtos.html')
    
    def test_listar_produto_em_falta_filtro(self):
        response = self.client.get(reverse('produtos:listar_produtos_falta'))
        self.assertEquals(len(response.context['lista_produtos']), 2)

    # def test_criar_produto_redirect_login(self):
    #     response = self.client.get(reverse('produtos:criar_produto'))
    #     self.assertRedirects(response, '/produtos/listar_produtos/?next=/produtos/criar_produto/')
    
    def test_criar_produto_template(self):
        login = self.client.login(username="testuser", password="123")

        response = self.client.get(reverse('produtos:criar_produto'))
        self.assertEquals(str(response.context['user']), 'testuser')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Produto/criar_produto.html')
    
    def test_criar_produto_altera_bd(self):
        login = self.client.login(username="testuser", password="123")

        dados_form = {
            'nome': 'Produto X',
            'fornecedor': 'Forn. Y',
            'preco_de_venda': 35.50
        }

        response = self.client.post(reverse('produtos:criar_produto'), dados_form)
        
        produto = Produto.objects.filter(
            nome= 'Produto X',
            fornecedor= 'Forn. Y',
            preco_de_venda= 35.50
        )

        self.assertTrue(len(produto) > 0)
        self.assertRedirects(response, reverse('produtos:listar_produtos'))
    
    def test_desconto_maximo(self):
        self.assertEquals(views.analisar_desconto_maximo(), 275.28)