from django.urls import path

from blog.views import blog_new, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blog'
urlpatterns = [
    path('', blog_new),
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete')
]