"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from backend.views import index
from api.views import HelloApi  # Our hello API
from htmx_spa.views import HtmxSpaView, HtmxFormsSpaView
from svelte_spa.views import SvelteSpaView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/hello", HelloApi.as_view()), # Our hello API
    path("svelte", SvelteSpaView.as_view(), name="svelte"), # Our Svelte SPA index view
    path("htmx", HtmxSpaView.as_view(), name="htmx"), # Our HTMX SPA index view
    path("htmx_forms", HtmxFormsSpaView.as_view(), name="htmx_forms"), # Our HTMX SPA Forms view
    path("", index, name="index"),
]
