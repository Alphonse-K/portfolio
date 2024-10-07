from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password):
        if not email:
            raise ValueError('Users must provide valid email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            username=username, 
            first_name=first_name, 
            last_name=last_name,
        )
        user.set_password(password)
        return user
    
    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(email, username, first_name, last_name, password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'