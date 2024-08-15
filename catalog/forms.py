from django.forms import ModelForm
from users.forms import StyleFormMixin
from catalog.models import Product, Version

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == 'казино' or 'криптовалюта' or 'крипта' or 'биржа' or 'дешево' or 'бесплатно' or 'обман' or 'полиция' or 'радар':
            raise forms.ValidationError('Недопустимое название товара')
        return name

class ProductModeratorForm(StyleFormMixin, ModelForm):
    def clean_description(self):
        cleaned_data = self.cleaned_data['title']
        if cleaned_data == 'казино' or 'криптовалюта' or 'крипта' or 'биржа' or 'дешево' or 'бесплатно' or 'обман' or 'полиция' or 'радар':
            raise forms.ValidationError('В описании продукта есть запрещённое слово')
        return cleaned_data

class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = '__all__'