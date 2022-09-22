from django.db import models
from deportes.models import Sport, Team, Competitor

class SportEventSingle(models.Model):
    start = models.DateTimeField(null=False)
    sport = models.ForeignKey(to=Sport, on_delete=models.CASCADE)
    competitors = models.ManyToManyField(to=Competitor)
    
    class Meta:
        ordering = ['-start']

class SportEventTeam(models.Model):
    start = models.DateTimeField(null=False)
    sport = models.ForeignKey(to=Sport, on_delete=models.CASCADE)
    teams = models.ManyToManyField(to=Team)
    
    class Meta:
        ordering = ['-start']