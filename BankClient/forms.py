from django import forms,aut
from .models import Client
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if not user:
                raise forms.ValidationError('Invalid email or password')

        return super().clean()
