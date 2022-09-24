from pyexpat import model
from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name
    

class Sport(models.Model):
    COMPETITOR_TYPE_CHOICES = (('team', 'Equipo'), ('single', 'Individual'))
    COMPETITION_TYPE_CHOICES = (('rounds', 'Eliminatoria'), ('score', 'Puntuacion'))

    name = models.CharField(max_length=50, null=False)
    competitor_type = models.CharField(max_length=15, choices=COMPETITOR_TYPE_CHOICES, default='team')
    competition_type = models.CharField(max_length=15, choices=COMPETITION_TYPE_CHOICES, default='rounds')

    class Meta:
        ordering = ['-name']
    
    def __str__(self):
        return self.name

class Competitor(models.Model):
    GENDER_CHOICES = (('male', 'Masculino'), ('female', 'Femenino'), ('other', 'Otro'))

    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default='other')
    sports = models.ManyToManyField(to=Sport)

    def __str__(self):
        return f'N: {self.name}\F:{self.faculty}'

class Team(models.Model):
    name = models.CharField(max_length=100, default='Sin Nombre')
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE)
    sport = models.ForeignKey(to=Sport, on_delete=models.CASCADE)
    members = models.ManyToManyField(to=Competitor)

    def __str__(self):
        if self.name != 'Sin Nombre':
            return f'N: {self.name}/nF: {self.faculty}/nD: {self.sport}'
        return f'F: {self.faculty}/nD: {self.sport}'

