from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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
                    "error": f"credenciais não autenticadas, corrija os campos e tente novamente!"
                },
            )
    @login_required
    def logout(request):
        logout(request)
        return redirect("financas:login")