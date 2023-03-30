from django import forms

class OperacionesForm(forms.Form):
    num1 = forms.IntegerField(label="Número 1")
    num2 = forms.IntegerField(label="Número 2")
    operaciones = [
        ("suma", "+"),
        ("resta", "-"),
        ("multiplicacion", "x"),
    ]
    operador = forms.ChoiceField(choices=operaciones, label="Operación")