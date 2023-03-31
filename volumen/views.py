from django.shortcuts import render
from .forms import VolumenForm
import numpy, math

def formulario(request):
    context = {
        'titulo': 'Calcular Volumen',
    }
    return render(request, 'volumen/formulario.html', context)
    
def mostrar(request):
    diametro = float(request.POST['diametro'])
    altura = float(request.POST['altura'])
    volumen = (numpy.pi * math.pow(diametro/2, 2) * altura)
    mostrar = 'El volumen del cilindro es de %f metros cúbicos' % (volumen)

    return render(request, "volumen/respuesta.html",{"mostrar": mostrar})


# Create your views here.
def calcular(request):
    mostrar = None
    if request.method == "POST":
        form = VolumenForm(request.POST)
        if form.is_valid():
            diametro = form.cleaned_data['diametro']
            altura = form.cleaned_data['altura']
            volumen = (numpy.pi * math.pow(diametro/2, 2) * altura)
            mostrar = 'El volumen del cilindro es de %f metros cúbicos' % (volumen)
    else:
        form = VolumenForm()
    return render(request, "respuesta.html", {"form": form, "mostrar": mostrar})