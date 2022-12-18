from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='posts/')
    tags = TaggableManager()
    
    def __str__(self):
        return self.title

    