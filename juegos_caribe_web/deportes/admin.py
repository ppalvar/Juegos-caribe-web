from django.contrib import admin
from . import models

@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(models.Competitor)
class CompetitorAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'age', 'gender',)
    search_fields = ('name', 'faculty',)
    list_filter = ('age', 'gender',)

@admin.register(models.Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'competitor_type',)
    search_fields = ('name',)

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'sport')
    search_fields = ('name', 'faculty', 'sport')

