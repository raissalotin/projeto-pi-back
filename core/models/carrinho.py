from django.db import models
from .user import User
from .pagamento import Pagamento
from .produto import Produto

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='carrinhos')
    pagamento = models.ForeignKey(Pagamento, on_delete=models.SET_NULL, blank=True, null=True)
    produtos = models.ManyToManyField(Produto, related_name='produto')

    def __str__(self):
        return f'Carrinho {self.id} - {self.usuario.user}'