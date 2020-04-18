from django.db import models

# Create your models here.
class OCRFile(models.Model):
    title = models.CharField(max_length=200)
    description =  models.TextField()

    # TODO: create a form to upload a file

    def __str__(self):
        """ A string representation of the model. """
        return self.title 
   
