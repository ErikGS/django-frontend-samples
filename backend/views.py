from django.http import HttpRequest
from django.shortcuts import render

def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title':'Django Frontend Samples',
            'message':'This is a default SSR django page.',
        }
    )