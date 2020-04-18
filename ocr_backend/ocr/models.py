from django.db import models

# Create your models here.
class OCR_file(models.Model):
    title = models.CharField(max_length=200)
    description =  models.TextField()
   
