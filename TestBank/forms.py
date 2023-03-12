from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from TestBank.models import UserAddress
from .constants import GENDER_CHOICE


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Not Selected')
)

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    


class UserRegistrationForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'on'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'autofocus':'off'}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

class UserAddressForm(forms.ModelForm):

    class Meta:
        model = UserAddress
        fields = [
            'street_address',
            'city',
            'postal_code',
            'country']