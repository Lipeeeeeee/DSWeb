import datetime
from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    texto = models.CharField(max_length = 256)
    data_pub = models.DateTimeField("Data de publicação")
    def __str__(self):
        return f"{self.texto} ({self.id})"
    def publicada_recentemente(self):
        agora = timezone.now()
        return agora - datetime.timedelta(hours = 24) <= self.data_pub <= agora
    publicada_recentemente.admin_order_field = "texto"
    publicada_recentemente.boolean = True
    publicada_recentemente.short_description = "Publiquei agora?"


class Alternativa(models.Model):
    texto = models.CharField(max_length = 256)
    votos = models.IntegerField("Quantidade de votos", default = 0)
    pergunta = models.ForeignKey(Pergunta, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.texto} ({self.id})"