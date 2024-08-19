from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.views import index, home, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
app_name = 'catalog'

urlpatterns = [
    path('', index),
    path('', home),
    path('', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete')
]