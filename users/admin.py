from django.contrib import admin
from .models import *


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderedProducts)
admin.site.register(Address)
admin.site.register(User)

