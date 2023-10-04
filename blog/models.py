from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from cloudinary.models import CloudinaryField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse("post-details", args=(str(self.id)))
        return reverse("home")
