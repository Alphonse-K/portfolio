from django.contrib.auth.backends import ModelBackend
from users.models import User


class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username, password ):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            if not user.is_active:        
                return user
            request.user = user
            return user
        return None