from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Not Selected')

]

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True,)
    address = models.CharField(max_length=100,default='belsh')
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'testbank_client'

