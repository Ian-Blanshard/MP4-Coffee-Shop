from django import forms
from .models import Discount


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['percentage']
        widgets = {
            'percentage': forms.Select(
                choices=[
                    (0, "0%"),
                    (5, "5%"),
                    (10, "10%"),
                    (15, "15%"),
                    (20, "20%"),
                    (25, "25%"),
                    (30, "30%"),
                    (35, "35%"),
                    (40, "40%"),
                    (45, "45%"),
                    (50, "50%"),
                ]
            )
        }
        labels = {
            'percentage': 'Please select a discount to apply to this product',
        }

    def __init__(self, *args, **kwargs):
        """ override the init and add product id to all id fields,
         this ensures they are unique when multiple forms are created in a loop"""
        product_id = kwargs.get('product_id', None)
        super().__init__(*args, **kwargs)
        if product_id:
            for field_name, field in self.fields.items():
                field.widget.attrs['id'] = f"{field_name}_{product_id}"
