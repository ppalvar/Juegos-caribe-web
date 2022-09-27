from django.urls import path
from .views import positions_list

app_name = 'medallero'
urlpatterns = [
    path('', positions_list, name='medallero'),
]
