from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()

    def __str__(self):
        return self.Name


class Stock(models.Model):
    Stock_name = models.CharField(max_length=100)
    Price = models.CharField(max_length=5)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Stock_name
