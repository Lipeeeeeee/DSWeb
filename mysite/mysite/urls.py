from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("enquetes/", include("enquetes.urls")),
    path("corridas/", include("corridas.urls")),
    path("financas/", include("financas.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("raiz.urls")),
]
