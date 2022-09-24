from django.contrib import admin
from . import models 

@admin.register(models.New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published',)
    search_fields = ('body', 'title')
