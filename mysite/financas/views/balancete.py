from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from financas.models.balancete import Balancete

@method_decorator(login_required, name="dispatch")
class BalanceteView(View):
    def get(request, **kwargs):
        balancete = Balancete.objects.get(pk=kwargs["pk"])
        return render(request, "financas/balancete.html", {"balancete": balancete})

    def post(request, *args, **kwargs):
        nome = request.POST["nome"]
        try:
            Balancete.objects.create(nome=nome, user=request.user.usuario)
            messages.success(request, "Balancete criado com sucesso!")
        except:
            messages.error(request, "Não foi possível criar balancete!")
        return redirect("financas:index")
