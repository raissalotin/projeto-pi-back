from django.db import models
from .categoria import Categoria 


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    cor = models.CharField(max_length=50, blank=True, null=True)
    tamanho = models.CharField(max_length=50, blank=True, null=True)
    categorias = models.ManyToManyField(Categoria, related_name='produtos')
    def __str__(self):
        return self.descricao
