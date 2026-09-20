from django.contrib import admin
from .models import Libro, Autor, FichaTecnica, Lector, Prestamo


class FichaTecnicaInline(admin.StackedInline):
    model = FichaTecnica
    can_delete = True
    extra = 0


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "isbn", "precio", "disponible")
    search_fields = ("titulo", "isbn")
    inlines = [FichaTecnicaInline]


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("libro", "lector", "fecha_prestamo", "fecha_devolucion_esperada", "estado")
    search_fields = ("libro__titulo", "lector__nombre")
    list_filter = ("estado", "fecha_prestamo")


admin.site.register(Autor)
admin.site.register(Lector)
