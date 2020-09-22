from django.db import models

from datetime import datetime, date
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # return reverse('post_url', kwargs={'pk': self.id} )
        return reverse('home',)

class Post(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=128, default='uncatgorized')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title +'   |   '+self.author.last_name
    
    def get_absolute_url(self):
        # return reverse('post_url', kwargs={'pk': self.id} )
        return reverse('home',)


