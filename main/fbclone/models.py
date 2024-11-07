from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    # Title of the post, max length is 100 characters
    title = models.CharField(max_length=100, verbose_name="post_title")
    
    # Content of the post, max length is 250 characters
    content = models.CharField(max_length=250, verbose_name="post_content")
    
    # Foreign key to the User model, linking each post to a specific user (author)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Date and time when the post was created, defaults to the current time
    date_posted = models.DateTimeField(default=timezone.now)
    
    # Image field for uploading images (optional field)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Field for image upload
    
    # File field for uploading videos (optional field)
    video = models.FileField(upload_to='videos/', blank=True, null=True)  # Add this line if you want a video field

    # String representation of the Post object, returns the title of the post
    def __str__(self):
        return self.title

    # Method to get the absolute URL for the post detail page
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
