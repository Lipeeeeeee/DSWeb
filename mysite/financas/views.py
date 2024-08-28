from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .models import Balancete, Transacao, Receita, Despesa

class BalanceteView(View):
    def get(self, request, *args, **kwargs):
        balancetes = Balancete.objects.all()
        return render(request, "financas/index.html", {"balancetes": balancetes})

    def post(request, *args, **kwargs):
        nome = request.POST["nome"]
        try:
            Balancete.objects.create(nome=nome, user_id=1)
        except Exception as error:
            return render(request, "financas/index.html", {"feedback": "Não foi possível criar balancete!"})
        return render(request, "financas/index.html", {"feedback": f"Balancete {nome} criado com sucesso!"})

    def get_balancete(request, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        return render(request, "financas/balancete.html", {"balancete": balancete})

class TransacaoView(View):
    def get(self, request, *args, **kwargs):
        nome_transacao = request.GET["pesquisa"]
        try:
            transacoes = Transacao.objects.filter(nome__contains=nome_transacao)
        except:
            return redirect('financas:index')
        return render(request, "financas/transacoes.html", {"transacoes": transacoes, "pesquisa": nome_transacao})

class ReceitaView(View):
    def get(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        return render(request, 'financas/receita.html', {'balancete': balancete})

    def post(request, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        valor = round(float(request.POST['valor']), 2)
        valor = valor if valor > 0 else valor * -1
        dados = {'nome': request.POST['nome'],
                 'valor': valor,
                 'boleto': request.POST['boleto'],
                 'balancete': balancete
                }
        try:
            Receita.objects.create(**dados)
            balancete.saldo += valor
            balancete.save()
            return redirect('financas:index')
        except:
            return render(request, "financas/index.html", {"feedback": "Não foi possível criar receita!"})

class DespesaView(View):
    def get(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs['pk'])
        return render(request, 'financas/despesa.html', {'balancete': balancete})

    def post(request, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        valor = round(float(request.POST['valor']), 2)
        valor = valor if valor < 0 else valor * -1
        dados = {'nome': request.POST['nome'],
                 'valor': valor,
                 'boleto': request.POST['boleto'],
                 'balancete': balancete
                }
        try:
            Despesa.objects.create(**dados)
            balancete.saldo += valor
            balancete.save()
            return redirect('financas:index')
        except:
            return render(request, "financas/index.html", {"feedback": "Não foi possível criar despesa!"})