# Generated by Django 2.2.12 on 2021-04-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_product_available_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_quantity',
            field=models.IntegerField(default=1),
        ),
    ]
