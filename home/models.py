from django.db import models
from cloudinary.models import CloudinaryField


class Employee(models.Model):
    featured_image = CloudinaryField('image', default='nobody')
    name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    bio = models.TextField()

    # ↓↓↓ CREDIT: Microsoft Copilot ↓↓↓

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"
    # ↑↑↑ CREDIT: Microsoft Copilot ↑↑↑

    def __str__(self):
        return self.full_name
