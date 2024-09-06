from django.urls import path
from .views.despesa import DespesaView
from .views.receita import ReceitaView
from .views.user import UserView
from .views.balancete import BalanceteView
from .views.transacao import TransacaoView

app_name = "financas"
urlpatterns = [
    path("", UserView.as_view(), name="login"),
    path("auth/", UserView.as_view(), name="authenticate"),
    path("logout/", UserView.logout, name="logout"),
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
