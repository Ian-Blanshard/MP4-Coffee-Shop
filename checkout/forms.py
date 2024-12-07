from django import forms
from django_countries.fields import CountryField
from .models import Order


class OrderForm(forms.ModelForm):

    country = CountryField().formfield()
    
    class Meta:
        model = Order
        # fields to include in form
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """Customize form"""
        super().__init__(*args, **kwargs)
        # add placeholders to replace labels
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }
        # start position for cursor
        self.fields['full_name'].widget.attrs['autofocus'] = True
        #set placeholders
        for field in self.fields:
            # dont put placeholder on for country dropdown
            if field != 'country':
                if self.fields[field].required:
                    # add star for reuqired fields
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            else:
                # set empty label for dropdown
                self.fields['country'].empty_label = 'Select Country'
            # remove labels
            self.fields[field].label = False