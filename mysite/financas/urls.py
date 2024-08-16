from django.urls import path
from . import views

app_name = "financas"
urlpatterns = [
    path("balancete/", views.BalanceteView.post, name="balancete"),
    path("balancete/<int:pk>/", views.BalanceteView.get_balancete, name="get_balancete"),
    path("", views.BalanceteView.as_view(), name="index"),
    path("receitas/<int:pk>/", views.ReceitaView.as_view(), name="receita"),
    path("receitas/<int:pk>/adicionar/", views.ReceitaView.post, name="adicionar_receita"),
    path("despesas/<int:pk>/", views.DespesaView.as_view(), name="despesa"),
    path("despesas/<int:pk>/adicionar/", views.DespesaView.post, name="adicionar_despesa"),
    path("pesquisar/", views.TransacaoView.as_view(), name="transacao")

]