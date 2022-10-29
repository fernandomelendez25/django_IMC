import json
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers
from .forms import CalcForm
from .models import Diagnostico
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