from django.db import models


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Not Selected')

]

class Client(models.Model):
 
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    number = models.CharField(max_length=50,null=True)
    active = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='N')
    adress = models.CharField(max_length=100,default=' ')
    city = models.CharField(max_length=50,default=' ')
    state = models.CharField(max_length=50,default=' ')
    zip_code = models.CharField(max_length=10,default=' ')
    password = models.CharField(max_length=50,default=' ')

    
    
    
    def __str__(self):
        return self.first_name