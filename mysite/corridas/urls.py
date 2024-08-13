from django.urls import path
from .views import CorridaView

app_name = "corridas"
urlpatterns = [
    path("", CorridaView.index, name="index"),
    path("calcular/", CorridaView.calculaValor, name="calculaCorrida"),
]