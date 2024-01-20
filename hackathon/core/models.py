from django.db import models
from django_resized import ResizedImageField


class Query(models.Model):
    
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    phone = models.IntegerField(null=True,blank=True)
    query = models.CharField(max_length=200 , null=True , blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=100, null=True , blank=True , default='Team GreenClean')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True , blank=True)
    post_picture = ResizedImageField(
        upload_to="post_images/", null=True, blank=True , default='')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title