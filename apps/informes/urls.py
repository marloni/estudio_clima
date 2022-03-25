from django.contrib import admin
from django.urls import include, path
from apps.informes.views import InformesView


urlpatterns = [
    path("", InformesView.as_view(), name="informes"),
    path("django_plotly_dash/", include("django_plotly_dash.urls")),
]
