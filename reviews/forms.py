from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        # fields to include in the form
        fields = ('review', 'rating')

    number_of_stars = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    rating = forms.ChoiceField(
        choices=number_of_stars,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Number of Stars (1 to 5)',
    )