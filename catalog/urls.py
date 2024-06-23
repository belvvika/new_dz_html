from django.urls import path

from catalog.views import index, home, ProductListView, ProductDetailView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', index),
    path('', home),
    path('', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('', BlogListView.as_view(), name='products_list'),
    path('products/<int:pk>/', BlogDetailView.as_view(), name='product_detail'),
    path('products/create', BlogCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update', BlogUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', BlogDeleteView.as_view(), name='product_delete')
]