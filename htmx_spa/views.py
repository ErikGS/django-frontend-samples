
import time
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def htmx(request):
    # Simulate some processing
    #time.sleep(0.5)
    # Processing End
    if request.htmx:
        return render(request, 'htmx_spa/components/dashboard.html')
    else:
        return render(request, 'htmx_spa/components/dashboard_full.html')

@login_required
def htmx_forms(request):
    # Simulate some processing
    #time.sleep(0.5)
    # Processing End
    if request.htmx:
        return render(request, 'htmx_spa/components/forms.html')
    else:
        return render(request, 'htmx_spa/components/forms_full.html')
