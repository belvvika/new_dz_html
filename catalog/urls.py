from django.urls import path
from catalog.views import index, home

urlpatterns = [
    path('', index),
    path('', home)
]