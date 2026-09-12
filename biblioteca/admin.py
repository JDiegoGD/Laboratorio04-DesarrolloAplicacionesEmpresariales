from django.contrib import admin
from .models import Libro, Autor, FichaTecnica, Lector, Prestamo

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(FichaTecnica)
admin.site.register(Lector)
admin.site.register(Prestamo)
