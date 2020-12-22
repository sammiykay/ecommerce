from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=23234232)
    first_name = models.CharField(max_length=23234232)
    last_name = models.CharField(max_length=23234232)
    email = models.CharField(max_length=23234232)


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=23234232)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name



    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=23234232)
    def __str__(self):
        return str(self.id)
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class View(models.Model):
    product= models.OneToOneField(Product, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0, blank=True, null=True)
    text = models.TextField()


    def __str__(self):
        return self.product.name

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=40)

    def __str__(self):
        return self.customer.name