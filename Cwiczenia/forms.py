from django import forms
from .models import Rekordy, Cwiczenia

class RekordForm(forms.ModelForm):

    class Meta:
        model = Rekordy
        fields = ('nazwa', 'cwiczenie', 'rekord_kg')