from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from financas.models.usuario import Usuario

class CadastroView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "financas/cadastro.html")
    
    def post(self, request, *args, **kwargs):
        try:
            dados = {"username": request.POST["username"], "senha": request.POST["password"]}
            user = User.objects.create(**dados)
            Usuario.objects.create(user=user)
        except:
            messages.error(request, "Não foi possível cadastrar esses dados, por favor tente novamente")
            redirect('cadastro')
        messages.success(request, "Usuário cadastrado com sucesso, pode entrar!")
        redirect('login')