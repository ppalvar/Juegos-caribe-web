from msilib.schema import File
from django.shortcuts import render
from noticias.models import New
from galeria.models import Image
from django.http import FileResponse

def index_view(request):
    latest_news = New.objects.all()[:5]
    last_image  = Image.objects.all()[0]

    context = {
        'latest_news':latest_news,
        'last_image':last_image
    }

    return render(request, 'index.html', context)
