from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='post_files', default='file')
    owner = models.ForeignKey(
        User, related_name='post', on_delete=models.CASCADE, null=True
    )
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
