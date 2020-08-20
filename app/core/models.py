from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# define class to overwrite standard input "username" with "email"
class UserManager(BaseUserManager):

    # extra_fields --> pass in all extra functions in additional fields
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Can't create user without email address")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password) # encrypts the password sha-256
        user.save(using=self._db) # good practice incase multiple db usage

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # uses special command

    objects = UserManager() # User manager for object

    USERNAME_FIELD = 'email'

