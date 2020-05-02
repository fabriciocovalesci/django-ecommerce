from django.conf import settings
from django.db import models
from django.utils import timezone

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=5,  decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    compra_data = models.DateTimeField(blank=True, null=True)
    foto = models.ImageField(
        upload_to='produtos', null=True, blank=True)

        
    def compra(self):
        self.compra_data = timezone.now()
        self.save()

    def precofinal(self):
        return self.quantidade * self.valor

    def __str__(self):
        return self.nome


    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"