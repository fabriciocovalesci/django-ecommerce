from django import forms
from loja.produtos.models import Produto

class AddProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "quantidade", "valor", "created_date", "foto"]


class CompraProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "quantidade", "valor", "created_date"]

