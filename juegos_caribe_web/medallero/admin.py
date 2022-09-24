from django.contrib import admin
from . import models

@admin.register(models.ResultTeamMatch)
class ResultTeamAdmin(admin.ModelAdmin):
    list_display = ('get_sport', 'get_start',)
    search_fields = ('get_sport',)

    @admin.display(ordering='-match__faculty')
    def get_faculty(self, obj):
        return obj.match.faculty

    @admin.display(ordering='-match__sport')
    def get_sport(self, obj):
        return obj.match.sport
    
    @admin.display(ordering='-match__start')
    def get_start(self, obj):
        return obj.match.start

@admin.register(models.ResultSingleMatch)
class ResultSingleAdmin(admin.ModelAdmin):
    list_display = ('get_sport', 'get_start',)
    search_fields = ('get_sport',)

    @admin.display(ordering='-match__faculty')
    def get_faculty(self, obj):
        return obj.match.faculty

    @admin.display(ordering='-match__sport')
    def get_sport(self, obj):
        return obj.match.sport
    
    @admin.display(ordering='-match__start')
    def get_start(self, obj):
        return obj.match.start
