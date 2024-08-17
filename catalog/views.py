from django.shortcuts import render
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def home(request):
    return render(request, 'products/home.html')

class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_dict = {}
        for product in Product.objects.all():
            for version in Version.objects.all():
                if version.indicates_current_version:
                    if version.product_id == int(product.pk):
                        version_dict[version.product_id] = version.version_name
        context_data['versions'] = version_dict
        return context_data


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')

    login_url = '/users/login/'
    redirect_field_name = '/'

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.author = user
        product.save()
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')

    login_url = '/users/login/'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method =='POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.author:
            return ProductForm
        if user.has_perm('catalog.can_cancel_publication_product') and user.has_perm('catalog.can_change_title_any_product') and user.has_perm('catalog.can_change_category_any_product'):
            return ProductModeratorForm
        raise PermissionDenied

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:products_list')

    login_url = '/users/login/'
    redirect_field_name = '/'
