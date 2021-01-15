from django.db import models
from category.models import Category


class Book(models.Model):
    bookName = models.CharField(null= False, blank= False, default= '', max_length= 25)
    bookPrice = models.IntegerField(null= False, blank= False)
    bookDescription = models.CharField(null= False, blank= False, default= '', max_length= 125)
    category = models.ForeignKey(Category, on_delete= models.RESTRICT)