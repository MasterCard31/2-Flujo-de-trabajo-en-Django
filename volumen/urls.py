from django.urls import path
from . import views

app_name = 'volumen'

urlpatterns = [
    # ex: /volumen/
    path('calcular/', views.calcular, name='calcular'),
    path('', views.formulario, name='formulario'),
    path('mostrar', views.mostrar, name='mostrar'),
    
]