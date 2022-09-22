from django.contrib import admin
from . import models

@admin.register(models.SportEventTeam)
class SportEventAdmin(admin.ModelAdmin):
    list_display = ('start', 'sport',)
    list_filter = ('start',)
    search_fields = ('sport',)

@admin.register(models.SportEventSingle)
class SportEventAdmin(admin.ModelAdmin):
    list_display = ('start', 'sport',)
    list_filter = ('start',)
    search_fields = ('sport',)
