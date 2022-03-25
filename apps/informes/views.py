from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from . import simpleexample


class InformesView(TemplateView):
    template_name = "informes.html"
    config = {"static_folder": "static", "routes_pathname_prefix": "/informes/"}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.POST.get("action") == "simpleexample":
            return redirect(simpleexample.app.server)
        return redirect(self.config["routes_pathname_prefix"])
