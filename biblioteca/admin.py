from django.contrib import admin
from .models import Libro, Autor, FichaTecnica, Lector, Prestamo


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "isbn", "precio", "disponible")
    search_fields = ("titulo", "isbn")


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("libro", "lector", "fecha_prestamo", "fecha_devolucion_esperada", "estado")
    search_fields = ("libro__titulo", "lector__nombre")
    list_filter = ("estado", "fecha_prestamo")


admin.site.register(Autor)
admin.site.register(FichaTecnica)
admin.site.register(Lector)
