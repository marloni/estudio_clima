from django.contrib import admin
from .models import Datos


class DatosAdmin(admin.ModelAdmin):
    list_display = (
        "year",
        "seq",
        "glide",
        "disaster_group",
        "disaster_subgroup",
        "disaster_type",
        "disaster_subtype",
        "event_name",
        "country",
        "iso",
        "region",
        "continent",
        "location",
        "associated_dis",
        "dis_mag_value",
        "dis_mag_scale",
        "start_data",
        "end_data",
        "total_deaths",
        "no_injured",
        "no_affected",
        "no_homeless",
        "total_affected",
        "total_damages",
    )
    search_fields = ("year", "seq")
    list_filter = ("year", "seq")


admin.site.register(Datos, DatosAdmin)
