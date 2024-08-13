from django.shortcuts import render
from .business import CalculaCorridaUberX, CalculaCorridaUberMoto, CalculaCorridaUberBlack, CalculaCorridaUberPool

class CorridaView():
    def index(request):
        return render(request, "corridas/index.html")

    def calculaValor(request):
        tipo = request.POST.get("tipoCorrida")
        km = request.POST.get("km")

        if not tipo or not km:
            return render(request, "corridas/index.html", {"error": "Por favor selecione o tipo da corrida e a quantidade de quilômetros!"})
        try:
            km = int(km)
            assert km > 0
        except:
            return render(request, "corridas/index.html", {"error": "Por favor selecione um número válido!"})

        if tipo == "x":
            corrida = CalculaCorridaUberX(km)
        elif tipo == "moto":
            corrida = CalculaCorridaUberMoto(km)
        elif tipo == "black":
            corrida = CalculaCorridaUberBlack(km)
        elif tipo == "pool":
            numPassageiros = int(request.POST.get("numPassageiros"))
            corrida = CalculaCorridaUberPool(km, numPassageiros=numPassageiros)

        valor = corrida.getValor()
        return render(request, "corridas/index.html", {"valor": valor})

