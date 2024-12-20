# Generated by Django 5.1.2 on 2024-11-26 16:01

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_remove_product_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='discount', serialize=False, to='products.product')),
                ('percentage', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
            ],
        ),
    ]
