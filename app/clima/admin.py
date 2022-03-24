from django.contrib import admin
from app.clima.models import Registro


class RegistroAdmin(admin.ModelAdmin):
    list_display = (
        "agnio",
        "subgrupo_desastres",
        "tipo_desastre",
        "subtipo_desastre",
        "nombre_evento",
        "pais",
        "iso",
        "region",
        "continente",
        "desastre_asociado",
        "magnitud_desastre",
        "escala_desastre",
        "fecha_inicio",
        "fecha_finalizacion",
        "total_muertes",
        "no_lesionados",
        "no_desaparecidos",
        "total_desaparecidos",
        "total_danos",
    )
    list_filter = (
        "tipo_desastre",
        "subgrupo_desastres",
        "escala_desastre",
        "continente",
        "region",
        "pais",
    )
    list_per_page = 50
    search_fields = (
        "agnio",
        "glide",
        "subgrupo_desastres",
        "tipo_desastre",
        "subtipo_desastre",
        "nombre_evento",
        "pais",
        "iso",
        "region",
        "continente",
        "ubicacion",
        "desastre_asociado",
        "magnitud_desastre",
        "escala_desastre",
        "fecha_inicio",
        "fecha_finalizacion",
        "total_muertes",
        "no_lesionados",
        "no_desaparecidos",
        "total_desaparecidos",
        "total_danos",
    )
    ordering = ("agnio",)
    date_hierarchy = "fecha_inicio"


admin.site.register(Registro, RegistroAdmin)
