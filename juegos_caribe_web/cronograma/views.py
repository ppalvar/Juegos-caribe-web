from django.shortcuts import render
from django.utils import timezone
from .models import SportEventSingle, SportEventTeam

from galeria import models


def cronogram_list(request):
    single_event = SportEventSingle.objects.all()
    team_event = SportEventTeam.objects.all()
    images = models.Image.objects.all()
    now_time = timezone.now()

    def order_by(a):
        return a[1].start

    single_event = [('single', e) for e in single_event]
    team_event = [('team', e) for e in team_event]
    sports_name = []

    events = list(single_event) + list(team_event)
    events.sort(key=order_by)

    for t, e in events:
        if not e.sport.name in sports_name:
            sports_name.append(e.sport.name)

    return render(request,
        'cronograma/cronograma.html',
        {'now_time': now_time,
        'sports_name': sports_name,
        'events': events,
        'images': images})

def cronogram_info(request, type_event, event_id):

    images = models.Image.objects.all()
    now_time = timezone.now()

    if type_event == 'single':

        single = SportEventSingle.objects.get(pk=event_id)

        return render(request,
            'cronograma/cronograma_info.html',
            {'now_time': now_time,
            'sport': single.sport,
            'date': single.start,
            'competitors': single.competitors.all(),
            'images': images})
    
    else:

        team = SportEventTeam.objects.get(pk=event_id)

        return render(request,
            'cronograma/cronograma_info.html',
            {'now_time': now_time,
            'sport': team.sport,
            'date': team.start,
            'competitors': team.teams.all(),
            'images': images})
