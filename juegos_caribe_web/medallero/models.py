from django.db import models
from deportes.models import Sport, Team, Competitor
from cronograma.models import SportEventSingle, SportEventTeam

class ResultTeamMatch(models.Model):
    match = models.OneToOneField(to=SportEventTeam, on_delete=models.CASCADE, related_name="result")
    positions = models.TextField()

class ResultSingleMatch(models.Model):
    match = models.OneToOneField(to=SportEventSingle, on_delete=models.CASCADE, related_name="result")
    positions = models.TextField()
