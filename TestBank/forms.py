from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Not Selected')
)

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    number = forms.CharField(max_length=15)
    amount = forms.DecimalField(decimal_places=2, max_digits=10)
    active = forms.BooleanField(required=False)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    zip_code = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'number', 'amount', 'active', 'gender', 'address', 'city', 'state', 'zip_code', 'password1', 'password2')