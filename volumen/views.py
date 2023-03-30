from django.shortcuts import render
from .forms import VolumenForm
import numpy, math

# Create your views here.
def calcular(request):
    mostrar = None
    if request.method == "POST":
        form = VolumenForm(request.POST)
        if form.is_valid():
            diametro = form.cleaned_data['diametro']
            altura = form.cleaned_data['altura']
            volumen = numpy.pi * math.pow(diametro/2, 2) * altura
            mostrar = 'El volumen del cilindro es de %i metros cúbicos' % (volumen)
    else:
        form = VolumenForm()
    return render(request, "respuesta.html", {"form": form, "mostrar": mostrar})