from django.contrib import admin
from .models.transacao import Transacao
from .models.receita import Receita
from .models.despesa import Despesa
from .models.usuario import Usuario
from .models.balancete import Balancete

admin.site.register(Balancete)
admin.site.register(Usuario)
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(Transacao)
