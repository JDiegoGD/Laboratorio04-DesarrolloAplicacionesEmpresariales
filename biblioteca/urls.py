from django.urls import path
from . import views

app_name = "biblioteca"

urlpatterns = [
    path("libros/", views.libro_list, name="libro_list"),
    path("libros/<int:pk>/", views.libro_detail, name="libro_detail"),
    path("autores/<int:pk>/", views.autor_detail, name="autor_detail"),
]
