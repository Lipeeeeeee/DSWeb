from django.shortcuts import render
from django.views import View
from .models import Balancete, Transacao

class BalanceteView(View):
    def index(self, request, *args, **kwargs):
        balancetes = Balancete.objects.all().order_by("-data")
        return render(request, "financas/index.html", {"balancetes": balancetes})

    def post(self, request, *args, **kwargs):
        nome = request.POST["nome"]
        try:
            Balancete.objects.create(nome=nome)
        except:
            return render(request, "financas/index.html", {"feedback": "Não foi possível criar balancete!"})
        return render(request, "financas/index.html", {"feedback": f"Balancete {nome} criado com sucesso!"})

    def get(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        return render(request, "financas/balancete.html", {"balancete": balancete})

class TransacaoView(View):
    def get(self, request, *args, **kwargs):
        nome_transacao = request.POST["pesquisa"]
        transacoes = Transacao.objects.filter(nome=nome_transacao)
        return render(request, "financas/transacoes.html", {"transacoes": transacoes})

class ReceitaView(View):
    def post(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        # perguntar como relacionar por código

class DespesaView(View):
    def post(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        # perguntar como relacionar por código