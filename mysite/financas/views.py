from django.shortcuts import render, redirect
from django.views import View
from .models import Balancete, Transacao, Receita, Despesa

class BalanceteView(View):
    def get(self, request, *args, **kwargs):
        balancetes = Balancete.objects.all().order_by("-data")
        return render(request, "financas/index.html", {"balancetes": balancetes})
    
    def post(request, *args, **kwargs):
        nome = request.POST["nome"]
        try:
            Balancete.objects.create(nome=nome)
        except Exception as error:
            return render(request, "financas/index.html", {"feedback": f"Não foi possível criar balancete! - {error}"})
        return redirect("financas:index")
    
    def get_balancete(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        return render(request, "financas/balancete.html", {"balancete": balancete})

class TransacaoView(View):
    def get(self, request, *args, **kwargs):
        nome_transacao = request.POST["pesquisa"]
        transacoes = Transacao.objects.filter(nome=nome_transacao)
        return render(request, "financas/transacoes.html", {"transacoes": transacoes})

class ReceitaView(View):
    def get(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        return render(request, 'financas/receita.html', {'balancete': balancete})

    def post(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        valor = int(request.POST['valor'])
        valor = valor if valor > 0 else valor * -1
        dados = {'nome': request.POST['nome'],
                 'valor': valor, 
                 'boleto': request.POST['boleto'],
                 'balancete': balancete
                }
        Receita.objects.create(**dados)
        redirect('index')

class DespesaView(View):
    def get(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs['pk'])
        return render(request, 'financas/despesa.html', {'balancete': balancete})

    def post(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        valor = int(request.POST['valor'])
        valor = valor if valor < 0 else valor * -1
        dados = {'nome': request.POST['nome'],
                 'valor': valor, 
                 'boleto': request.POST['boleto'],
                 'balancete': balancete
                }
        Despesa.objects.create(**dados)
        redirect('index')