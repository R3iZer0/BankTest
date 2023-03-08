from django.contrib.auth.backends import BaseBackend
from .models import Client

class ClientBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            client = Client.objects.get(email=email)
            if client.check_password(password):
                return client
        except Client.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None
