from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES = (
    ('Province No 1','Province No 1'),
    ('Province No 2','Province No 2'),
    ('Bagmati Province', 'Bagmati Province'),
    ('Gandaki Province', 'Gandaki Province'),
    ('Lumbani Province', 'Lumbani Province'),
    ('Karnali Province', 'Karnali Province'),
    ('Sudurpashchim Province', 'Sudurpashchim Province'),

)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICE = (
    ('M', 'Mobile'),
    ('L','Laptop'),
    ('TW', 'Top Ware'),
    ('BW','Bottom Ware'),
)

class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

def __str__(self):
    return str(self.id)

@property
def total_cost(self):
    return self.quantity * self.product.discounted_price

STATE_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Deliverd','Deliverd'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices = STATE_CHOICES,default='Pending')


