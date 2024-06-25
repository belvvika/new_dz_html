from django.urls import path

from catalog.views import index, home, ProductListView, ProductDetailView

urlpatterns = [
    path('', index),
    path('', home),
    path('', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]