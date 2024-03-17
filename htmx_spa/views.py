from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HtmxSpaView(LoginRequiredMixin, TemplateView):
    template_name = "htmx_spa/index.html"

class HtmxFormsSpaView(LoginRequiredMixin, TemplateView):
    template_name = "htmx_spa/forms_full.html"