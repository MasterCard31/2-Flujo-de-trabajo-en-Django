from django.shortcuts import render

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
        'suma' : '+',
        'resta' : '-',
        'multiplicacion': 'x',

    }
    return render(request, 'operaciones.html', context)

def mostrar(request):
    
    context = {
        'suma' : '+',
        'resta' : '-',
        'multiplicacion': 'x',
        'num1': request.GET['num1'],
        'operador': request.GET['operador'],
        'num2' : request.GET['num2'],
        'resultado': '',
    }
    return render(request, 'respuesta.html', context )
    

