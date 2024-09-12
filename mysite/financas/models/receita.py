from django.db import models
from .transacao import Transacao


class Receita(models.Model):
    transacao = models.OneToOneField(
        Transacao, on_delete=models.CASCADE, related_name="rec"
    )

    def __str__(self):
        return f"{self.__class__.__name__}: {self.transacao.nome} - R$ {self.transacao.valor:.2f}"
