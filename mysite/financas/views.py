from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Balancete, Transacao, Receita, Despesa


class BalanceteView(View):
    def get(self, request, *args, **kwargs):
        balancetes = Balancete.objects.all()
        return render(request, "financas/index.html", {"balancetes": balancetes})

    def post(request, *args, **kwargs):
        nome = request.POST["nome"]
        try:
            Balancete.objects.create(nome=nome, user=request.user)
        except:
            return render(
                request,
                "financas/index.html",
                {"feedback": "Não foi possível criar balancete!"},
            )
        return redirect("financas:index")

    def get_balancete(request, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        return render(request, "financas/balancete.html", {"balancete": balancete})


class TransacaoView(View):
    def get(self, request, *args, **kwargs):
        nome_transacao = request.GET["pesquisa"]
        try:
            transacoes = Transacao.objects.filter(
                nome__contains=nome_transacao, balancete__user=request.user
            )
        except:
            return redirect("financas:index")
        return render(
            request,
            "financas/transacoes.html",
            {"transacoes": transacoes, "pesquisa": nome_transacao},
        )


class ReceitaView(View):
    def get(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        return render(request, "financas/receita.html", {"balancete": balancete})

    def post(request, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        valor = round(float(request.POST["valor"]), 2)
        valor = valor if valor > 0 else valor * -1
        dados = {
            "nome": request.POST["nome"],
            "valor": valor,
            "boleto": request.POST["boleto"],
            "balancete": balancete,
        }
        try:
            Receita.objects.create(**dados)
            balancete.saldo += valor
            balancete.save()
            return redirect("financas:index")
        except:
            return render(
                request,
                "financas/index.html",
                {"feedback": "Não foi possível criar receita!"},
            )


class DespesaView(View):
    def get(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        return render(request, "financas/despesa.html", {"balancete": balancete})

    def post(request, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        valor = round(float(request.POST["valor"]), 2)
        valor = valor if valor < 0 else valor * -1
        dados = {
            "nome": request.POST["nome"],
            "valor": valor,
            "boleto": request.POST["boleto"],
            "balancete": balancete,
        }
        try:
            Despesa.objects.create(**dados)
            balancete.saldo += valor
            balancete.save()
            return redirect("financas:index")
        except:
            return render(
                request,
                "financas/index.html",
                {"feedback": "Não foi possível criar despesa!"},
            )


class UserView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "financas/login.html")

    def post(self, request, *args, **kwargs):
        credenciais = {
            "username": request.POST["login"],
            "password": request.POST["senha"],
        }
        user = authenticate(request, **credenciais)
        if user:
            login(request, user)
            return redirect("financas:index")
        else:
            return render(
                request,
                "financas/login.html",
                {
                    "error": f"credenciais {credenciais['login']} e {credenciais['senha']} não autenticadas, corrija os campos e tente novamente!"
                },
            )

    def logout(request):
        logout(request)
        return redirect("financas:login")
