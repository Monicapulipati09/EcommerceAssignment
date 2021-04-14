# Generated by Django 2.2.12 on 2021-04-08 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product_discription', models.TextField()),
                ('product_image', models.CharField(blank=True, max_length=5000, null=True)),
                ('available_quantity', models.IntegerField()),
            ],
        ),
    ]