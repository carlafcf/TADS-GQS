from django.urls import path

from Produto import views

app_name = 'produtos'

urlpatterns = [
    path('criar-produto/', views.criar_produto, name='criar_produto'),
    path('listar-produtos/', views.listar_produtos, name='listar_produtos'),
    path('listar-produtos-falta/', views.listar_produtos_falta, name='listar_produtos_falta'),
    path('detalhes/<int:pk>', views.detalhes_produto, name='detalhes_produto'),
    
]