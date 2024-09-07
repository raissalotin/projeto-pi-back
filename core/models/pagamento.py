from django.db import models

from .user import User

class Pagamento(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    usuario = models.ForeignKey(User,
                                on_delete=models.PROTECT,
                                  related_name="pagamento")
    status = models.IntegerField(choices=StatusCompra.choices,  default=StatusCompra.CARRINHO)

def __str__(self):
    return f'Pagamento {self.id} - {self.get_status_display()} para {self.usuario}'
