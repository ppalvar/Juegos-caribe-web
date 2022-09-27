from functools import wraps
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .loader import *

def search_when_post(func):
    @wraps(func)
    def decorated(request : HttpRequest, *args, **kwargs):
        if request.method == 'POST':
            query = request.POST['query']
            results = search(query)
            return render(request, 'search_engine/search.html', {'results': results})
        return func(request, *args, **kwargs)
    return decorated
