from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
#from cloudinary.models import CloudinaryField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_posts",)

    def total_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse("post-details", args=(str(self.id)))
        return reverse('home')
