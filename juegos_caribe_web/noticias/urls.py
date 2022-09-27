from django.urls import path
from .views import news_list_view, news_detail_view

app_name = 'noticias'
urlpatterns = [
    path('', news_list_view, name='noticias_list'),
    path('<str:slug>/', news_detail_view, name='noticias_detail')
]
