from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_discription = models.TextField()
    product_image = models.ImageField(null= True, blank=True)
    available_quantity = models.IntegerField(default= 1)
 

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    order_id = models.CharField(max_length=200, default = 1)
    ordered_date = models.DateTimeField(default = datetime.now())
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def get_total_cart_value(self):
        orderitems = self.orderedproducts_set.all()
        total = sum([item.get_total_item_price for item in orderitems])
        return total

    @property
    def get_total_items(self):
        orderitems = self.orderedproducts_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderedProducts(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null = True, blank= True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def get_total_item_price(self):
        total = self.quantity * self.product.price
        return total


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)


class User(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)