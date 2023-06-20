# Generated by Django 3.2.19 on 2023-06-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('fornecedor', models.CharField(max_length=200, verbose_name='Fornecedor')),
                ('qnt_em_estoque', models.PositiveIntegerField(null=True, verbose_name='Quantidade em estoque')),
                ('preco_de_venda', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço de venda')),
                ('desconto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Desconto')),
                ('favorito', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['nome', 'fornecedor'],
            },
        ),
    ]