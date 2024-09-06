from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from financas.models.transacao import Transacao

@method_decorator(login_required, name="dispatch")
class TransacaoView(View):
    def get(self, request, *args, **kwargs):
        nome_transacao = request.GET["pesquisa"]
        try:
            transacoes = Transacao.objects.filter(
                nome__contains=nome_transacao, balancete__user=request.user.usuario
            )
        except:
            return redirect("financas:index")
        return render(
            request,
            "financas/transacoes.html",
            {"transacoes": transacoes, "pesquisa": nome_transacao},
        )