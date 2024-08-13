import datetime
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase
from .models import Pergunta

def criar_pergunta(texto, qtd_dias):
    data = timezone.now() + datetime.timedelta(days = qtd_dias)
    return Pergunta.objects.create(texto = texto, data_pub = data)

class IndexViewTest(TestCase):
    def test_sem_pergunta(self):
        """
        Sem perguntas cadastradas - DEVE exibir mensagem correspondente
        """
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertQuerysetEqual(resposta.context['lista_enquetes'], [])
        self.assertContains(resposta, 'Nenhuma enquete cadastrada até o momento!')
        self.assertEqual(resposta.status_code, 200)

    def test_pergunta_passado(self):
        """
        Com pergunta no passado - DEVE exibir o link para a enquete na lista
        """
        criar_pergunta('Pergunta no passado', -1)
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Pergunta no passado")
        self.assertQuerysetEqual(resposta.context["lista_enquetes"], ["<Pergunta: Pergunta no passado (1)>"])

class PerguntaModelTest(TestCase):
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