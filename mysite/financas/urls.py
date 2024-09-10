from django.urls import path
from django.contrib.auth import views as auth
from .views.despesa import DespesaView
from .views.receita import ReceitaView
from .views.balancete import BalanceteView
from .views.transacao import TransacaoView
from .views.index import IndexView

app_name = "financas"
urlpatterns = [
    path("", auth.LoginView.as_view(), name="login"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    path("balancetes/", BalanceteView.as_view(), name="adicionar_balancete"),
    path("balancete/<int:pk>/", BalanceteView.as_view(), name="balancete"),
    path("inicio/", IndexView.as_view(), name="index"),
    path("receita/<int:pk>/", ReceitaView.as_view(), name="receita"),
    path(
        "receitas/<int:pk>/adicionar/", ReceitaView.as_view(), name="adicionar_receita"
    ),
    path("despesa/<int:pk>/", DespesaView.as_view(), name="despesa"),
    path(
        "despesas/<int:pk>/adicionar/", DespesaView.as_view(), name="adicionar_despesa"
    ),
    path("pesquisar/", TransacaoView.as_view(), name="transacoes"),
]
