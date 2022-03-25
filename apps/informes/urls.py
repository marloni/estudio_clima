from django.contrib import admin
from django.urls import include, path
from apps.informes.views import InformesView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", InformesView.as_view(), name="informes"),
]
