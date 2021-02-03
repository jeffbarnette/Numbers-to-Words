from django.urls import path
from .views import num_to_english, service_test

urlpatterns = [
    path('', service_test, name='service_test'),
    path('num_to_english', num_to_english, name='num_to_english'),
]