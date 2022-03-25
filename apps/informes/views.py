from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class InformesView(TemplateView):
    template_name = "informes.html"
    context_object_name = "informes"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        return redirect("/")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
