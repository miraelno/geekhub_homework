# Generated by Django 5.0 on 2024-01-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
