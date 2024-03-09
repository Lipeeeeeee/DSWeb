from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Disciplina: DS Web<br>Semestre: 2024.1<br>Matrícula: 20231014040027<br>Nome: Felipe Alves de Vasconcelos</h1>")