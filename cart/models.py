from django.contrib.auth.models import User
from django.db import models
from book.models import Book
from users.models import Users


class Cart(models.Model):
    book = models.ForeignKey(Book, on_delete= models.RESTRICT)
    user = models.ForeignKey(Users, on_delete= models.RESTRICT)
    bought = models.BooleanField(null= False, blank= False, default= False)