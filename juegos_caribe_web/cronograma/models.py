from django.db import models
from deportes.models import Sport, Team, Competitor

class SportEventSingle(models.Model):
    start = models.DateTimeField(null=False)
    sport = models.ForeignKey(to=Sport, on_delete=models.CASCADE)
    competitors = models.ManyToManyField(to=Competitor)
    
    class Meta:
        ordering = ['-start']
    
    def __str__(self):
        ans = ''
        for s in self.competitors.all():
            ans = f'{ans} | {s}'
        return ans

class SportEventTeam(models.Model):
    start = models.DateTimeField(null=False)
    sport = models.ForeignKey(to=Sport, on_delete=models.CASCADE)
    teams = models.ManyToManyField(to=Team)
    
    class Meta:
        ordering = ['-start']

    def __str__(self):
        ans = ''
        for s in self.teams.all():
            ans = f'{ans} | {s}'
        return ans
