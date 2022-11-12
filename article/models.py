from django.conf import settings
from django.db import models
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, default="kauy", null=True, blank=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article:article_home')

class Article(models.Model):
    title = models.CharField(max_length=255)
    article_image = models.ImageField(null=True, blank=True,upload_to="images/article/")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,null=True, blank=True
    )
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='article_post')

    def total_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article:article_home')