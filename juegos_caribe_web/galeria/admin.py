from django.contrib import admin
from . import models

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('description',)
    list_filter  = ('description',)
