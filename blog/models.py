from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=255)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Difficulty(models.Model):
    level = models.CharField(max_length=255)
        
    def __str__(self):
        return self.level

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default="food")
    difficulty = models.CharField(max_length=255, default="medium")
    body = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_posts",)


    def total_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)