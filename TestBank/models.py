from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    active = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name