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
    
