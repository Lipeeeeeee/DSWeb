from django.urls import path
from django.contrib.auth import views as auth
from .views.despesa import DespesaView
from .views.receita import ReceitaView
from .views.balancete import BalanceteView
from .views.transacao import TransacaoView

app_name = "financas"
urlpatterns = [
    path("", auth.LoginView.as_view(), name="login"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    path("balancete/", BalanceteView.post, name="balancete"),
    path(
        "balancete/<int:pk>/", BalanceteView.get_balancete, name="get_balancete"
    ),
    path("inicio/", BalanceteView.as_view(), name="index"),
    path("receitas/<int:pk>/", ReceitaView.as_view(), name="receita"),
    path(
        "receitas/<int:pk>/adicionar/", ReceitaView.post, name="adicionar_receita"
    ),
    path("despesas/<int:pk>/", DespesaView.as_view(), name="despesa"),
    path(
        "despesas/<int:pk>/adicionar/", DespesaView.post, name="adicionar_despesa"
    ),
    path("pesquisar/", TransacaoView.as_view(), name="transacao"),
]
