# Generated by Django 5.1.2 on 2024-12-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_reviews_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
