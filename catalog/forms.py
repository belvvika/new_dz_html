from django.forms import ModelForm

from catalog.models import Product, Version
from django.forms import BooleanField
class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for self.file_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == 'казино' or 'криптовалюта' or 'крипта' or 'биржа' or 'дешево' or 'бесплатно' or 'обман' or 'полиция' or 'радар':
            raise forms.ValidationError('Недопустимое название товара')
        return name

class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'category', 'published_sign')

# class ProductModeratorForm(StyleFormMixin, ModelForm):
#     def clean_description(self):
#         cleaned_data = self.cleaned_data['title']
#         if cleaned_data == 'казино' or 'криптовалюта' or 'крипта' or 'биржа' or 'дешево' or 'бесплатно' or 'обман' or 'полиция' or 'радар':
#             raise forms.ValidationError('В описании продукта есть запрещённое слово')
#         return cleaned_data

class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = '__all__'