from django.urls import path
from . import views

app_name = 'volumen'

urlpatterns = [
    # ex: /volumen/
    path('', views.calcular, name='calcular'),
    
]