# Generated by Django 4.1.7 on 2023-07-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_remove_product_favorite_product_product_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='chosen',
            field=models.BooleanField(default=False),
        ),
    ]