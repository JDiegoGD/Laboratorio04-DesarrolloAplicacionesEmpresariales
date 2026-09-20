from django.contrib import admin
from .models import Libro, Autor, FichaTecnica, Lector, Prestamo


class FichaTecnicaInline(admin.StackedInline):
    model = FichaTecnica
    can_delete = True
    extra = 0


class PrestamoInline(admin.TabularInline):
    model = Prestamo
    extra = 0
    fields = (
        "lector",
        "fecha_prestamo",
        "fecha_devolucion_esperada",
        "fecha_devolucion_real",
        "estado",
    )
    readonly_fields = ("fecha_prestamo",)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "isbn", "precio", "disponible")
    search_fields = ("titulo", "isbn")
    inlines = [FichaTecnicaInline, PrestamoInline]


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("libro", "lector", "fecha_prestamo", "fecha_devolucion_esperada", "estado")
    search_fields = ("libro__titulo", "lector__nombre")
    list_filter = ("estado", "fecha_prestamo")


admin.site.register(Autor)
admin.site.register(Lector)
