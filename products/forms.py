from django import forms
from django.contrib import messages
from .widgets import CustomClearableFileInput
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

    def clean_sku(self):
        """check the sku is unique when is valid is called"""
        sku = self.cleaned_data.get('sku')
        if Product.objects.filter(sku=sku).exists():
            messages.error(self.request, 'This SKU is already in use. Please use a different SKU.')
        return sku