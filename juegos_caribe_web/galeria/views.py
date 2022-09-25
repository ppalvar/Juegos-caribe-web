from django.shortcuts import render
from . import models

def gallery_view(request):
    images = models.Image.objects.all()

    return render(request, 'galeria/galeria.html', {'images' : images})
