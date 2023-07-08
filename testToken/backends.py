from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class TokenBackend(BaseBackend):
    def authenticate(self, request, token=None, **kwargs):
        try:
            user = User.objects.get(id=2) # for testing process only!!!
            return user
        except User.DoesNotExist:
            return None
