from django.contrib import admin
from .models import *


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(View)
admin.site.register(ContactUs)
admin.site.register(Shipping)

# Register your models here.