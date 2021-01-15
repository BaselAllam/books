from django.db import models



class Category(models.Model):
    categoryName = models.CharField(null= False, blank= False, default= '', max_length= 25)
    categoryId = models.AutoField(null= False, blank= False, primary_key= True, auto_created= True)


    def __str__(self):
        return self.categoryName