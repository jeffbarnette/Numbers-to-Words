"""config URL Configuration"""
from django.contrib import admin
from django.urls import path, include

from core.views import num_to_english

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
