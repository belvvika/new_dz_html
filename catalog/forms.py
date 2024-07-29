from django.forms import ModelForm

from catalog.models import Product, Version

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = '__all__'