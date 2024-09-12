from django.shortcuts import render
from financas.models.balancete import Balancete
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name="dispatch")
class IndexView(View):
    def get(self, request, *args, **kwargs):
        balancetes = Balancete.objects.all()
        return render(request, "financas/index.html", {"balancetes": balancetes})
