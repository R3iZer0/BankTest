from django import forms
from .models import Client



GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Not Selected')
)

class ClientForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES)


class ClientForm(forms.ModelForm):
    error_messages = {
        'required': 'This asd is required.',
    }
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'number', 'amount','active','gender','adress','city','state','zip_code']
