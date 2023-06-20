from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from Produto.models import Produto
from Produto.forms import ProdutoForm


def listar_produtos(request):
    lista_produtos = Produto.objects.all()

    informacoes = {
        'lista_produtos': lista_produtos
    }

    return render(request, 'Produto/listar_produtos.html', informacoes)

class ListarProdutos(ListView):
    model = Produto
    # Definir nome, senão será usado "object"
    context_object_name = 'lista_produtos'
    template_name = 'Produto/listar_produtos.html'

def listar_produtos_falta(request):
    produtos = Produto.objects.filter(qnt_em_estoque=0)

    informacoes = {
        'lista_produtos': produtos
    }

    return render(request, 'Produto/listar_produtos.html', informacoes)

class ListarProdutosFalta(ListView):
    model = Produto
    # Definir nome, senão será usado "object"
    context_object_name = 'lista_produtos'
    template_name = 'Produto/listar_produtos.html'

    def get_queryset(self):
        produtos = Produto.objects.filter(qnt_em_estoque=0)
        return produtos


@login_required
def criar_produto(request):
    if (request.method == 'POST'):
        form = ProdutoForm(request.POST)
        if (form.is_valid()):
            nome = form.cleaned_data['nome']
            fornecedor = form.cleaned_data['fornecedor']
            preco_de_venda = form.cleaned_data['preco_de_venda']
            Produto.objects.create(
                nome=nome,
                fornecedor=fornecedor,
                preco_de_venda=preco_de_venda
            )
            return redirect('produto:listar')
    else:
        form = ProdutoForm()

    informacoes = {
        'form': form
    }

    return render(request, 'Produto/criar_produto.html', informacoes)

class CriarProduto(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'Produto/criar_produto.html'
    success_url = reverse_lazy('produto:listar')


def analisar_desconto_maximo():
    produtos = Produto.objects.all()

    desconto_maximo = 0

    for produto in produtos:
        valor_desconto = round(float(produto.preco_de_venda) * (float(produto.desconto) / 100), 2)
        if (valor_desconto > desconto_maximo):
            desconto_maximo = valor_desconto

    return desconto_maximo


def detalhes_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    informacoes = {
        'produto': produto
    }
    return render(request, 'Produto/detalhes_produto.html', informacoes)

class DetalhesProduto(DetailView):
    model = Produto
    context_object_name = 'produto'
    template_name = 'Produto/detalhes_produto.html'