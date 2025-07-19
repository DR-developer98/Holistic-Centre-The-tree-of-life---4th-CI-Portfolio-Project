from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Employee(models.Model):

    name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    bio = models.TextField()
	
    def __str__ (self):
	    return self.name

