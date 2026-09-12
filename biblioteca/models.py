from django.db import models


# ============================================================
# EJERCICIO 1 — Entidad principal recuperada de la Semana 3
# ============================================================
# Este es el modelo que ya existía en el laboratorio anterior.
# A partir de aquí se agregan las tres relaciones nuevas.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)

    # --- 1:N ---

    autor = models.ForeignKey(
        "Autor",
        on_delete=models.PROTECT, 
        related_name="libros",
        null=True,
        blank=True,
    )

    # --- N:M ---
    lectores = models.ManyToManyField(
        "Lector",
        through="Prestamo",
        related_name="libros_leidos",
        blank=True,
    )

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo


# ============================================================
# EJERCICIO 2 — Relación 1:1 (ficha complementaria)
# ============================================================

class FichaTecnica(models.Model):
    libro = models.OneToOneField(
        Libro,
        on_delete=models.CASCADE,
        related_name="ficha_tecnica",
    )
    sinopsis = models.TextField()
    numero_paginas = models.PositiveIntegerField()
    idioma_original = models.CharField(max_length=50)
    edicion = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Ficha técnica de {self.libro.titulo}"


# ============================================================
# EJERCICIO 3 — Relación 1:N (Autor -> Libros)
# ============================================================
class Autor(models.Model):
    nombre_completo = models.CharField(max_length=150)
    nacionalidad = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.nombre_completo


# ============================================================
# EJERCICIO 4 — Relación N:M con modelo intermedio
# ============================================================
class Lector(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    ESTADOS = [
        ("PRESTADO", "Prestado"),
        ("DEVUELTO", "Devuelto"),
        ("ATRASADO", "Atrasado"),
    ]

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name="prestamos",
    )
    lector = models.ForeignKey(
        Lector,
        on_delete=models.CASCADE,
        related_name="prestamos",
    )

    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion_esperada = models.DateField()
    fecha_devolucion_real = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default="PRESTADO")

    class Meta:
        ordering = ["-fecha_prestamo"]

    def __str__(self):
        return f"{self.libro.titulo} -> {self.lector.nombre} ({self.estado})"
