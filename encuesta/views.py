from django.shortcuts import render
from .forms import OperacionesForm

# Create your views here.
def index(request):
    context = {
        'titulo': 'Formulario',
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context = {
        'titulo': 'Respuesta',
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'email': request.POST['email'],
        'website': request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)

def operaciones(request):
    context = {
        'titulo': 'Operaciones básicas',
    }
    return render(request, 'forma1/operaciones.html', context)

def mostrar(request):
    num1 = Float(request.POST['num1'])
    num2 = Float(request.POST['num2'])
    operador = request.POST['operador']

    if operador == "suma":
        resultado = num1 + num2
        mostrar = 'El suma de %f + %f = %f' % (num1, num2, resultado)
    elif operador == "resta":
        resultado = num1 - num2
        mostrar = 'El resta de %f - %f = %f' % (num1, num2, resultado)
    elif operador == "multiplicacion":
        resultado = num1 * num2
        mostrar = 'El multiplicación de %f x %f = %f' % (num1, num2, resultado)

    context = {
        'mostrar': mostrar,
    }
    return render(request, 'forma1/respuesta.html', context )

# Segunda forma
def calcular(request):
    result = None
    if request.method == "POST":
        form = OperacionesForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operador = form.cleaned_data['operador']
            if operador == "suma":
                result = num1 + num2
            elif operador == "resta":
                result = num1 - num2
            elif operador == "multiplicacion":
                result = num1 * num2
    else:
        form = OperacionesForm()
    return render(request, "forma2/calcular.html", {"form": form, "result": result})
            
        
    

