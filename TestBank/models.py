from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Not Selected')

]

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    active=models.BooleanField(default=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=3)

