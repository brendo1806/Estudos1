from django import forms
from .models import Controle

class ControleForm(forms.ModelForm):
    class Meta:
        model= Controle
        fields = '__all__'
