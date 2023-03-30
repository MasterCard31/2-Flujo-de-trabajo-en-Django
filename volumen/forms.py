from django import forms

class VolumenForm(forms.Form):
    """VolumenForm definition."""
    diametro = forms.FloatField(label="Introduzca el diámetro en metros")
    altura = forms.FloatField(label="Introduzca la altura en metros")

    # TODO: Define form fields here
