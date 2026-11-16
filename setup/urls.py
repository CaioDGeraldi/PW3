from django.contrib import admin
from django.urls import include, path
from integracao import views

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("api/consulta-cep/<str:cep>/", views.buscar_cep, name="buscar_cep"),
    path("admin/", admin.site.urls),
]
