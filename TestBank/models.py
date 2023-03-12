from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import AbstractUser
from .constants import GENDER_CHOICE

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Not Selected')

]

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    number = models.CharField(max_length=50,null=True)
    active = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='N')
    city = models.CharField(max_length=50,default=' ')
    state = models.CharField(max_length=50,default=' ')
    zip_code = models.CharField(max_length=10,default=' ')
    password = models.CharField(max_length=50,default=' ')

    def __str__(self):
        return self.first_name


class UserAddress(models.Model):

    street_address = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=256)

    def __str__(self):
        return self.user.email
