from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Aplicação de <u>Enquetes</u> - DSWeb 2024.1</h1>")