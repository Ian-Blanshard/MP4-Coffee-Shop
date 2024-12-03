from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        # fields to include in the form
        fields = ('review', 'rating')