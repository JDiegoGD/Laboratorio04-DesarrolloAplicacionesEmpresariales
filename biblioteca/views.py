from django.shortcuts import render, get_object_or_404
from .models import Libro, Autor


def libro_detail(request, pk):
    libro = get_object_or_404(
        Libro.objects.select_related("autor", "ficha_tecnica").prefetch_related(
            "prestamos__lector"
        ),
        pk=pk,
    )
    return render(request, "biblioteca/libro_detail.html", {"libro": libro})


def libro_list(request):
    libros = Libro.objects.select_related("autor").prefetch_related(
        "prestamos__lector"
    )
    return render(request, "biblioteca/libro_list.html", {"libros": libros})


def autor_detail(request, pk):
    autor = get_object_or_404(
        Autor.objects.prefetch_related("libros"),
        pk=pk,
    )
    return render(request, "biblioteca/autor_detail.html", {"autor": autor})
