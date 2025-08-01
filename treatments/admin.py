from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Treatment


@admin.register(Treatment)
class TreatmentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug')
    search_fields = ['name', 'content']
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)
