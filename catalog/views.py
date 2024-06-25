
from django.shortcuts import render, get_object_or_404


from django.views.generic import ListView, DetailView

from catalog.models import Product


# Create your views here.

def index(request):
    return render(request, 'catalog/index.html')

def home(request):
    return render(request, 'catalog/home.html')

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product
