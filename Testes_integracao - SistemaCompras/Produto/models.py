from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome")
    fornecedor = models.CharField(max_length=200, verbose_name="Fornecedor")
    qnt_em_estoque = models.PositiveIntegerField(verbose_name="Quantidade em estoque", null=True)
    preco_de_venda = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço de venda")
    desconto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Desconto", null=True, blank=True)
    favorito = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome', 'fornecedor']