from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "Usuário"

class Balancete(models.Model):
    nome = models.CharField("Nome do balancete", max_length=30, unique=True)
    data = models.DateField("Data de criação do balancete", auto_now_add=True)
    saldo = models.FloatField("Saldo total do balancete", default=0)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    class Meta:
        ordering = ["-data"]

class Transacao(models.Model):
    nome = models.CharField("Nome da transação", max_length=30)
    valor = models.FloatField("Valor da transação")
    boleto = models.ImageField("Foto do boleto da transação", upload_to="", width_field="10", height_field="30", null=True, blank=True)
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transações"

class Receita(Transacao):
    ...
    

class Despesa(Transacao):
    ...