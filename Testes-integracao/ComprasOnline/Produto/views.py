from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Produto.models import Produto
from Produto.forms import ProdutoForm

def listar_produtos(request):
    produtos = Produto.objects.all()

    informacoes = {
        'lista_produtos': produtos
    }

    return render(request, 'Produto/listar_produtos.html', informacoes)

def listar_produtos_falta(request):
    produtos = Produto.objects.filter(qnt_em_estoque=0)

    informacoes = {
        'lista_produtos': produtos
    }

    return render(request, 'Produto/listar_produtos.html', informacoes)

# @login_required
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
            return redirect('produtos:listar_produtos')
    else:
        form = ProdutoForm()
    
    informacoes = {
        'form': form
    }

    return render(request, 'Produto/criar_produto.html', informacoes)

def analisar_desconto_maximo():
    produtos = Produto.objects.all()

    desconto_maximo = 0

    for produto in produtos:
        valor_desconto = round(float(produto.preco_de_venda) * (float(produto.desconto)/100), 2)
        if (valor_desconto > desconto_maximo):
            desconto_maximo = valor_desconto
    
    return desconto_maximo

def detalhes_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    informacoes = {
        'produto': produto
    }
    return render(request, 'Produto/detalhes_produto.html', informacoes)