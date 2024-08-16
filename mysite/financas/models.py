from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Balancete(models.Model):
    nome = models.CharField("Nome do balancete", max_length=30)
    data = models.DateField("Data de criação do balancete", auto_now_add=True)
    saldo = models.FloatField("Saldo total do balancete", default=0)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Transacao(models.Model):
    ...

class Receita(Transacao):
    nome = models.CharField("Nome da receita", max_length=30)
    valor = models.FloatField("Valor da receita")
    boleto = models.ImageField("Foto do boleto da receita", width_field="10", height_field="30", null=True, unique=True)
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE)

class Despesa(Transacao):
    nome = models.CharField("Nome da despesa", max_length=30)
    valor = models.FloatField("Valor da despesa")
    boleto = models.ImageField("Foto do boleto da despesa", width_field="10", height_field="30", null=True, unique=True)
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE)
