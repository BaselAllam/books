from django.db import models
from category.models import Category
from django.urls import reverse

class Book(models.Model):
    bookName = models.CharField(null= False, blank= False, default= '', max_length= 25)
    bookPrice = models.IntegerField(null= False, blank= False)
    bookDescription = models.CharField(null= False, blank= False, default= '', max_length= 125)
    category = models.ForeignKey(Category, on_delete= models.RESTRICT)
    # bookCover = models.ImageField(upload_to = 'media/media/')
    publishedDate = models.DateField(null= False, blank= False, auto_now= True)


    def __str__(self):
        return self.bookName
    


    def get_absolute_url(self):
        return reverse("book_details", kwargs={"id": self.id})
    