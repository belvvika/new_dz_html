
from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy, reverse
from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'preview_picture', 'date_created', 'published_sign', 'views_counter')
    success_url = reverse_lazy('catalog:products_list')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'preview_picture', 'date_created', 'published_sign', 'views_counter')
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:products_list')