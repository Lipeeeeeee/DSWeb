from django.db import models
from .usuario import Usuario

class Balancete(models.Model):
    nome = models.CharField("Nome do balancete", max_length=30, unique=True)
    data = models.DateTimeField("Data de criação do balancete", auto_now_add=True)
    saldo = models.FloatField("Saldo total do balancete", default=0)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["-data"]