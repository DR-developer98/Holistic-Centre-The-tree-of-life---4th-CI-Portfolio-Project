from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Employee

# Register your models here.
admin.site.register(Employee)
