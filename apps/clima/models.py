from django.db import models
from django.contrib.auth.models import User


# Año     Glide 	Subgrupo de Desastres 	Tipo de Desastre 	Subtipo de Desastre 	Nombre del Evento 	País 	ISO 	Región 	Continente 	Ubicación 	Desastre asociado 	Magnitud del Desastre 	Escala del Desastre 	Fecha de Inicio 	Fecha de Finalización 	Total de Muertes 	No. de Lesionados 	No. de Desaparecidos 	No. de Desmovilizados 	Total de Desaparecidos 	Total de Daños


class Registro(models.Model):
    """
    Modelo para la tabla clima
    """

    # año
    agnio = models.IntegerField(blank=True, null=True, verbose_name="Año")
    glide = models.CharField(max_length=50, blank=True, null=True, verbose_name="Glide")
    subgrupo_desastres = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Subgrupo de Desastres"
    )
    tipo_desastre = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Tipo de Desastre"
    )
    subtipo_desastre = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Subtipo de Desastre"
    )
    nombre_evento = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Nombre del Evento"
    )
    pais = models.CharField(max_length=50, blank=True, null=True, verbose_name="País")
    iso = models.CharField(max_length=50, blank=True, null=True, verbose_name="ISO")
    region = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Región"
    )
    continente = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Continente"
    )
    ubicacion = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Ubicación"
    )
    desastre_asociado = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Desastre asociado"
    )
    magnitud_desastre = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Magnitud del Desastre"
    )
    escala_desastre = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Escala del Desastre"
    )
    fecha_inicio = models.DateField(
        blank=True,
        null=True,
        verbose_name="Fecha de Inicio",
        help_text="Formato: dd/mm/yyyy",
    )
    fecha_finalizacion = models.DateField(
        blank=True,
        null=True,
        verbose_name="Fecha de Finalización",
        help_text="Formato: dd/mm/yyyy",
    )
    total_muertes = models.IntegerField(
        blank=True, null=True, verbose_name="Total de Muertes"
    )
    no_lesionados = models.IntegerField(
        blank=True, null=True, verbose_name="No. de Lesionados"
    )
    no_desaparecidos = models.IntegerField(
        blank=True, null=True, verbose_name="No. de Desaparecidos"
    )
    no_desmovilizados = models.IntegerField(
        blank=True, null=True, verbose_name="No. de Desmovilizados"
    )
    total_desaparecidos = models.IntegerField(
        blank=True, null=True, verbose_name="Total de Desaparecidos"
    )
    total_danos = models.IntegerField(
        blank=True, null=True, verbose_name="Total de Daños"
    )

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        ordering = ["agnio"]

    def __str__(self):
        return str(self.agnio)
