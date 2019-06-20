from django.db import models
from django.contrib.auth.models import User,PermissionsMixin
from django.contrib  import  auth

# Create your models here.
class User(auth.models.User, PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)