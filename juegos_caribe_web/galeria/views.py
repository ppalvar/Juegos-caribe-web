from urllib import request
from django.shortcuts import render
from . import models
from search_engine.decorators import search_when_post

@search_when_post
def gallery_view(request):
    images = models.Image.objects.all()

    return render(request, 'galeria/galeria.html', {'images' : images})
