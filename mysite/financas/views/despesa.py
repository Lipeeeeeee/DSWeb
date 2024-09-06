from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from financas.models.balancete import Balancete
from financas.models.transacao import Transacao
from financas.models.despesa import Despesa

@method_decorator(login_required, name="dispatch")
class DespesaView(View):
    def get(self, request, *args, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        return render(request, "financas/despesa.html", {"balancete": balancete})

    def post(request, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        valor = float(request.POST["valor"])
        dados = {
            "nome": request.POST["nome"],
            "valor": valor,
            "boleto": request.POST["boleto"],
            "balancete": balancete,
        }
        try:
            transacao = Transacao.objects.create(**dados)
            Despesa.objects.create(transacao=transacao)
            balancete.saldo -= valor
            balancete.save()
            return redirect("financas:index")
        except Exception as e:
            return render(
                request,
                "financas/index.html",
                {"feedback": f"Não foi possível criar despesa! {e}"},
            )