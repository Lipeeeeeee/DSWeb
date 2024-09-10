from django.db import models
from .transacao import Transacao


class Despesa(models.Model):
    transacao = models.OneToOneField(
        Transacao, on_delete=models.CASCADE, related_name="des"
    )

    def __str__(self):
        return f"{self.__class__.__name__}: {self.transacao.nome} - R$ {self.transacao.valor:.2f}"
