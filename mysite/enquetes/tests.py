import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Pergunta

class PerguntaTestes(TestCase):
    def test_publicada_recentemente_retorna_false_futura(self):
        """
        O método deve retornar FALSE em caso de datas futuras
        """
        tempo = timezone.now() + datetime.timedelta(seconds=1)
        p = Pergunta(data_pub=tempo)
        self.assertIs(p.publicada_recentemente(), False)

    def test_publicada_recentemente_retorna_true(self):
        """
        O método deve retornar TRUE em caso de datas das últimas 24 horas
        """
        tempo = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        p = Pergunta(data_pub=tempo)
        self.assertIs(p.publicada_recentemente(), True)

    def test_publicada_recentemente_retorna_false_antiga(self):
        """
        O método deve retornar FALSE em caso de datas antigas (data < últimas 24 horas)
        """
        tempo = timezone.now() - datetime.timedelta(hours=24, seconds=1)
        p = Pergunta(data_pub=tempo)
        self.assertIs(p.publicada_recentemente(), False)