from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SvelteSpaView(LoginRequiredMixin, TemplateView):
    template_name = "svelte_spa/index.html"
