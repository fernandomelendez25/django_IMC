from django import forms
from django.forms import ModelForm
from .models import Diagnostico
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Make a form for the calculator

class CalcForm(ModelForm):
    class Meta:
        model = Diagnostico
        fields = ('estatura', 'peso')
        help_texts = {
            'estatura': _('Ingresa tu estatura en metros.'),
            'peso': _('Ingresa tu peso en kilogramos.'),
        }
        
class CustomUserForm(UserCreationForm):
    pass