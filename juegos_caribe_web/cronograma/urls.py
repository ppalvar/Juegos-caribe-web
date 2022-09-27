from django.urls import path
from .views import cronogram_list, cronogram_info

app_name = 'cronograma'
urlpatterns = [
    path('', cronogram_list, name='cronograma'),
    path('<str:type_event>/<int:event_id>', cronogram_info, name="cronograma_info")
]
