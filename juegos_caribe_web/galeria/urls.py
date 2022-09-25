from . import views
from django.urls import path

app_name = 'galeria'
urlpatterns = [
    path('', view=views.gallery_view, name='galeria'),
]
