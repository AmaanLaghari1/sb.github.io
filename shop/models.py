from django.db.models import Avg
from django.conf import settings
from django.db import models
from datetime import datetime

# Create your models here.

CATEGORY_CHOICES = (
                ('', 'Select an option'),
                ('C', 'clothing'), #First one is the value of select option and second is the displayed value in option
                ('E', 'electronics'),
                ('G', 'groceries'),
                ('HA', 'home accessories'),
                )
SUB_CATEGORY_CHOICES = (
    ('', 'Select an option'),
    ('men','men'),
    ('women','women'),
    ('mob','mobile'),
    ('com','computer'),
    ('machine','machinery'),
    ('tv','television'),
    ('furn','furniture'),
    ('kitc','kitchen'),
)

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    product_name = models.CharField(max_length=60)
    description = models.CharField(max_length=400)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
    sub_category = models.CharField(max_length=25, choices=SUB_CATEGORY_CHOICES, blank=True, null=True)
    price = models.IntegerField(default=0)
    bulk_quantity = models.IntegerField(default=0)
    bulk_price = models.IntegerField(default=0)
    seller_contact = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.id}: {self.product_name}"

    def num_of_reviews(self):
        return self.prorating_set.count()

    def average_rating(self):
        return self.prorating_set.aggregate(Avg('rate'))['rate__avg']

class Pimage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='shop/images/')

    def __str__(self):
        return self.product.product_name

class ProRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    review = models.CharField(max_length=250)
    rate = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.product_name}"
    
    def total_price(self):
        return self.quantity*self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # or_items = models.ForeignKey(OrderItem, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    bill_address = models.ForeignKey('PlacedOrder', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    recieved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def cart_total(self):
        total = 0 
        for orders in self.items.all():
            total += orders.total_price()
        return total
    
COUNTRY = (
    ('', 'Select Country'),
    ('1', 'Pakistan')
)
CITY = (
    ('', 'Select City'),
    ('1', 'Hyderabad')
)
    
class PlacedOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, blank=True, null=True)
    contact = models.CharField(max_length=11)
    address = models.TextField(max_length=150)
    address2 = models.TextField(max_length=150)
    country = models.CharField(max_length=15, choices=COUNTRY, default='Pakistan')
    city = models.CharField(max_length=15, choices=CITY, default="Hyderabad")
    zip_code = models.CharField(max_length=8)

    def __str__(self):
        return self.user.username