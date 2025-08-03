from django.db import models

# Create your models here


class Enquiry(models.Model):

    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created_on = models.TimeField(auto_now_add=True)
    # ↓↓↓ CREDIT: I think therefore I blog, Code Institute Project ↓↓↓
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]
    # ↑↑↑ CREDIT: I think therefore I blog Code Institute Project ↑↑↑

    def __str__(self):
        return f"Enquiry from {self.name}"
