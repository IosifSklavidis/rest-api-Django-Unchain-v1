from django.db import models

# these are the basic classes when i want to override/customize
# the default django user model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# Create the manager for the UserProfile model
class UserProfileManager(BaseUserManager):
    # Manager for user profiles

    def create_user(self, email, name, password=None):
        # Create a new user profile
        if not email:
            raise ValueError("Users must have email address")

        email = self.normalize_email(email)
        # creates a new model that user manager is representing
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
            # Create and save a new superuser with the given details
            user = self.create_user(email, name, password)

            user.is_superuser = True
            user.is_staff = True
            user.save(using=self._db)

            return user

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    # Database model for users in the system
    # this says that i need an email colunmn in my DB UserProfile table
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # customize the manager for the user model
    objects = UserProfileManager()

    # override the current email and use the given user_email from the model
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # Retrieve full name of the users
        return self.name

    def get_short_name(self):
            # Retrieve short name of the users
            return self.name

    def __str__():
        # return string representation of the users
        return self.email

class ProfileFeedItem(models.Model):
    # Profile status update
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return the model as a string
        return self.status_text
