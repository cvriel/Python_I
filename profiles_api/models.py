from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email adres")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """database models for users in the systems"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objectss = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """ Retrieve full name of user """
        return self.name

    def get_short_name(self):
        """ Retrieve shot name of user"""
        return self.name

    def __str__(self):
        """ Return string representation of our user """
        return self.email


class ProfileFeedItem(models.Model):
    """ Profile status update """

    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        """ Return string representation of the feed """
        return self.status_text
