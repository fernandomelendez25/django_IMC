from django.urls import path
from .views import CalculatorView, CalcAndSaveView, Nav

app_name = "calculator"

urlpatterns = [
    path('', CalculatorView.as_view(), name="home"),
    path('calcandsave/', CalcAndSaveView.as_view(), name="calcandsave"),
    path('nav/', Nav.as_view(), name="nav"),
]