from django.db import models
from home.models import Employee
from cloudinary.models import CloudinaryField


class Treatment(models.Model):
    featured_image = CloudinaryField('image', default='placeholder-treatment')
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    duration = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    practitioner = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="treatments")

    def __str__ (self):
        return self.name
