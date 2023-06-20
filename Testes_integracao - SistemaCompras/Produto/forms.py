from django.forms import ModelForm
from django.core.exceptions import ValidationError

from Produto.models import Produto


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'fornecedor', 'preco_de_venda']

    def clean(self):
        cleaned_data = super().clean()

        nome = self.cleaned_data['nome']
        fornecedor = self.cleaned_data['fornecedor']

        produtos_existentes = Produto.objects.filter(nome=nome, fornecedor=fornecedor)

        if (len(produtos_existentes) > 0):
            raise ValidationError("Já há um produto deste fornecedor com este nome cadastrado.")