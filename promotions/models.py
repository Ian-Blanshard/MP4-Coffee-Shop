from django.db import models
from django.core.validators import MaxValueValidator
from products.models import Product

class Discount(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='discount', primary_key=True)
    percentage = models.PositiveIntegerField(validators=[MaxValueValidator(50)])

    def apply_discount(self, price):
        """Calculate discounted price."""
        discounted_price = price - (price * self.percentage / 100)
        return round(discounted_price, 2)
    
    def discounted_price(self):
        """get the discounted price to display in template"""
        return self.apply_discount(self.product.price)

    def __str__(self):
        return f"{self.percentage}% off"
