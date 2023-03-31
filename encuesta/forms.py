from django import forms

class OperacionesForm(forms.Form):
    num1 = forms.FloatField(label="Número 1")
    num2 = forms.FloatField(label="Número 2")
    operaciones = [
        ("suma", "+"),
        ("resta", "-"),
        ("multiplicacion", "x"),
    ]
    operador = forms.ChoiceField(choices=operaciones, label="Operación")