from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory

from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def home(request):
    return render(request, 'products/home.html')

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')

    def get_context_data(self, **kwargs):
        ''' Метод для вывода формы версии при редактировании продукта '''
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method =='POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        ''' Метод для сохранения формы при редоктировании '''
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:products_list')