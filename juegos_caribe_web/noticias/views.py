from django.shortcuts import render, get_object_or_404
from .models import New
from search_engine.decorators import search_when_post

@search_when_post
def news_list_view(request):
    all_news = New.objects.all()

    return render(request, 'noticias/noticias_list.html', {'all_news' : all_news})

@search_when_post
def news_detail_view(request, slug):
    new = get_object_or_404(New, slug=slug)
    
    return render(request, 'noticias/noticias_detail.html', {'new' : new}) 
