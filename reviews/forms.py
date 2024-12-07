from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        # fields to include in the form
        fields = ('review', 'rating')

    number_of_stars = [
        (5, '5 - Excellent'),
        (4, '4 - Very Good'),
        (3, '3 - Good'),
        (2, '2 - Fair'),
        (1, '1 - Poor'),
    ]

    rating = forms.ChoiceField(
        choices=number_of_stars,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Number of Stars (1 to 5)',
    )