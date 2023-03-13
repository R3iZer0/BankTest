from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from .models import Client
from .constants import GENDER_CHOICE

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Not Selected')
)


class ClientRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    zip_code = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'address', 'city', 'state', 'zip_code']

    def save(self, commit=True):
        user = super(ClientRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        client_group = Group.objects.get(name='Client')
        client_group.user_set.add(user)
        client_profile = Client.objects.create(
            user=user,
            address=self.cleaned_data['address'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            zip_code=self.cleaned_data['zip_code'],
        )
        return user