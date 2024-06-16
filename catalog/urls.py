from django.urls import path

from catalog.views import index, home, products_list, product_detail

urlpatterns = [
    path('', index),
    path('', home),
    path('', products_list, name='products_list'),
    path('products/<int:pk>/', product_detail, name='product_detail')
]