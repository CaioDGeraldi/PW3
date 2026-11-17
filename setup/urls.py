from django.contrib import admin
from django.urls import path
from integracao import views

urlpatterns = [
    path("api/consulta-cep/<str:cep>/", views.buscar_cep, name="buscar_cep"),
    path("admin/", admin.site.urls),
]
