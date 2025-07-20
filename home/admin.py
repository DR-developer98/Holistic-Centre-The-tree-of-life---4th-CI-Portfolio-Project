from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(SummernoteModelAdmin):

    list_display = ('name', 'last_name', 'slug')
    search_fields = ['name', 'last_name']
    prepopulated_fields = {'slug': ('name', 'last_name')}
    summernote_fields = ('bio',)