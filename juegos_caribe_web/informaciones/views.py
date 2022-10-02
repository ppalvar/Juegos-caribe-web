from msilib.schema import File
from statistics import mode
from django.shortcuts import render
from noticias.models import New
from galeria.models import Image
from cronograma.models import SportEventSingle, SportEventTeam
from django.utils.timezone import now

def index_view(request):
    latest_news = New.objects.all()[:5]
    last_image  = Image.objects.all()[0]
    next_matches= list(SportEventSingle.objects.all()) + list(SportEventTeam.objects.all())

    next_matches.sort()
    
    next_matches = next_matches[:5]

    context = {
        'latest_news':latest_news,
        'last_image':last_image,
        'next_matches':next_matches,
        'now':now,
    }

    return render(request, 'index.html', context)
