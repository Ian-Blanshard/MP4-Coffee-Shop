from django.db import models
from products.models import Product
from profiles.models import UserProfile
from django.core.validators import MinValueValidator, MaxValueValidator

class Reviews(models.Model):
    """model for reviews"""

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False, related_name='reviews')
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=False, blank=False, related_name='reviews'
    )
    review = models.TextField(max_length=1000, blank=True)
    rating = models.FloatField(validators=[MinValueValidator(
        1), MaxValueValidator(5)], null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Review by {self.user} for {self.product} - Rating: {self.rating}"

