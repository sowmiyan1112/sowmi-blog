from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(default='slug')
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(blank=True, null=True, upload_to='media/')
    image2=models.ImageField(blank=True, null=True, upload_to='media/')
    number=models.IntegerField(blank=True, null =True)
    para=models.TextField(default="para")
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:200]


 

    

