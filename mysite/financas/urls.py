from django.urls import path
from . import views

app_name = "financas"
urlpatterns = [
    path("balancete/", views.BalanceteView.post, name="post_balancete"),
    path("balancete/<int:pk>/", views.BalanceteView.get, name="get_balancete"),
    path("", views.BalanceteView.index, name="index"),
    path("receitas/<int:pk>", views.ReceitaView.post, name="post_receita"),
    path("despesas/<int:pk>", views.DespesaView.post, name="post_despesa"),
    path("pesquisar/", views.TransacaoView.get, name="get_transacao")

]