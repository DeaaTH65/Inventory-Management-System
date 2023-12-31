from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    count = models.IntegerField()

    def __str__(self):
        return self.name
    
    
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} purchased {self.quantity} {self.product.name}"   