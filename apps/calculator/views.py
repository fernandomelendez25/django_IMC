from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

class CalculatorView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'calculator.html', context)
    
    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            data = self.request.POST
            print(data)
            return JsonResponse(data, safe=False)
        return JsonResponse({"error": "Not a valid request"}, status=400)