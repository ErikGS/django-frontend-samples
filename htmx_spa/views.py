
import time
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def htmx(request):
    # Simulate some processing
    #time.sleep(0.5)
    # Processing End
    if request.htmx:
        return render(request, 'htmx_spa/components/dashboard.html')
    else:
        return render(request, 'htmx_spa/components/dashboard_full.html')

def htmx_forms(request):
    # Simulate some processing
    #time.sleep(0.5)
    # Processing End
    if request.htmx:
        return render(request, 'htmx_spa/components/forms.html')
    else:
        return render(request, 'htmx_spa/components/forms_full.html')
