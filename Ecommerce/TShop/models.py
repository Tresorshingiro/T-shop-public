from django.db import models
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    release_date = models.DateField()
    is_available = models.BooleanField(default=True)
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.name
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)