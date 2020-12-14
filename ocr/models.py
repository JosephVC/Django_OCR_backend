from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='post_files', default='file')
    uploaded = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='uploaded')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='post', on_delete=models.CASCADE
    )
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
