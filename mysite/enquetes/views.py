from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Pergunta, Alternativa


def index(request):
    lista = Pergunta.objects.filter(data_pub__lte=timezone.now()).order_by("-data_pub")
    return render(request, "enquetes/index.html", {"lista_enquetes": lista})

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    return render(request, "enquetes/detalhes.html", {"enquete": pergunta})

def votacao(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    try:
        alternativa_id = request.POST["escolha"]
        alternativa = pergunta.alternativa_set.get(pk = alternativa_id)
    except (KeyError, Alternativa.DoesNotExist):
        contexto = {"enquete": pergunta, "error": "Você precisa selecionar uma alternativa"}
        return render(request, "enquetes/detalhes.html", contexto)
    else:
        alternativa.votos += 1
        alternativa.save()
        return HttpResponseRedirect(reverse("enquetes:resultado", args = (pergunta.id, )))

def resultado(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    return render(request, "enquetes/resultado.html", {"enquete": pergunta})