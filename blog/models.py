from django.db import models
from django.utils import timezone

# Create your models here.

#title
#image
#datecreated
#updatedat
#viewscount
#author
#content
#category


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']



class Article(models.Model):
    title = models.CharField(max_length=55, unique=True)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    viewscount = models.IntegerField(default=0)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
    class Meta:
        ordering = ['-created_at']
