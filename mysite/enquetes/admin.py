from django.contrib import admin
from .models import Pergunta, Alternativa

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 2

class PerguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Pergunta", {"fields": ["texto"]}),
        ("Data de publicação", {"fields": ["data_pub"]}),
    ]
    inlines = [AlternativaInline]
    list_filter = ["data_pub"]
    list_display = ("id", "texto", "data_pub", "publicada_recentemente")
    search_fields = ["texto"]

admin.site.register(Pergunta, PerguntaAdmin)
#admin.site.register(Alternativa)