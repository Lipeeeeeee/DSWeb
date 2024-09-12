from django.db import models
from .balancete import Balancete


class Transacao(models.Model):
    nome = models.CharField("Nome da transação", max_length=30)
    valor = models.FloatField("Valor da transação")
    boleto = models.ImageField(
        "Foto do boleto da transação",
        null=True,
        blank=True,
        default="../media/Teste.png",
    )
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transações"
