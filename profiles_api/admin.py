from django.contrib import admin

# Register your models here.
from profiles_api import models

# this enables the user to register as a admin
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
