# Generated by Django 5.0 on 2024-01-02 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_delete_productmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]