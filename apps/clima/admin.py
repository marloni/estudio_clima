from dataclasses import field
from re import A
from django.contrib import admin
from apps.clima.models import Registro, Datos


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

    fieldsets = (
        ("Año", {"fields": ("agnio",)}),
        (
            "Desastre",
            {"fields": ("subgrupo_desastres", "tipo_desastre", "subtipo_desastre", "nombre_evento",),},  # Campos
        ),
        ("Ubicación", {"fields": ("pais", "iso", "continente", "region", "ubicacion",)},),
        ("Desastre asociado", {"fields": ("desastre_asociado", "magnitud_desastre", "escala_desastre",)},),
        ("Fechas", {"fields": ("fecha_inicio", "fecha_finalizacion",)},),
        ("Muertes", {"fields": ("total_muertes", "no_lesionados")}),
        ("Desaparecidos", {"fields": ("no_desaparecidos", "total_desaparecidos")}),
        ("Daños", {"fields": ("total_danos",)}),
    )


admin.site.register(Registro, RegistroAdmin)
admin.site.register(Datos)
