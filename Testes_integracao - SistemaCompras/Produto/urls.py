from django.urls import path

from Produto import views

app_name = 'produto'

urlpatterns = [
    path('criar/', views.criar_produto, name='criar'),
    path('criar-cbv/', views.CriarProduto.as_view(), name='criar_cbv'),

    path('listar/', views.listar_produtos, name='listar'),
    path('listar-cbv/', views.ListarProdutos.as_view(), name='listar_cbv'),

    path('listar-falta/', views.listar_produtos_falta, name='listar_falta'),
    path('listar-falta-cbv/', views.ListarProdutosFalta.as_view(), name='listar_falta_cbv'),

    path('detalhes/<int:pk>', views.detalhes_produto, name='detalhes'),
    path('detalhes-cbv/<int:pk>', views.DetalhesProduto.as_view(), name='detalhes_cbv'),

]