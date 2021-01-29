from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class Users(AbstractUser):
    email = models.EmailField(null= False, blank= False, unique= True)


    USERNAME_FIELD =  'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()