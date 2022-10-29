import json
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import JsonResponse
from django.core import serializers
from .forms import CalcForm, CustomUserForm
from .models import Diagnostico
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.


# Vistas para el calculo del IMC y almacenamiento en la base de datos
class CalculatorView(View):
    def get(self, request, *args, **kwargs):
        form = CalcForm()
        context = {
            'form': form
        }
        return render(request, 'calculadora/calcSend.html', context)

    def post(self, request, *args, **kwargs):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            try:
                data = json.loads(request.body)
                imc = Diagnostico.objects.create(
                    estatura=float(data['estatura']),
                    peso=float(data['peso'])
                )
                imc.save()
                data = serializers.serialize('json', [imc, ])
                print(data)
                return JsonResponse({'imc': imc.imc, 'imc_class': imc.estado}, status=200)
            except (Exception) as e:
                return JsonResponse({'error': 'Error al calcular el IMC'}, status=400)
        return JsonResponse({"error": "Not a valid request"}, status=400)


class MainCalculatorView(View):
    def get(self, request, *args, **kwargs):
        form = CalcForm()
        context = {
            'form': form
        }
        return render(request, 'calculadora/localCalculator.html', context)

# Vistas para visualizar los datos de la base de datos

# Vistas de login y registro de usuarios


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserForm()
        context = {
            'form': form
        }
        return render(request, 'registration/signup.html', context)

    def post(self, request, *args, **kwargs):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(to='calculator:home')