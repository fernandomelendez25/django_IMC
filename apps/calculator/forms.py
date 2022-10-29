from django import forms
from django.forms import ModelForm
from .models import Diagnostico
from django.utils.translation import gettext_lazy as _

# Make a form for the calculator

class CalcForm(ModelForm):
    class Meta:
        model = Diagnostico
        fields = ('estatura', 'peso')
        help_texts = {
            'estatura': _('Ingresa tu estatura en metros.'),
            'peso': _('Ingresa tu peso en kilogramos.'),
        }
        