from django.urls import path
from .views import CalculatorView, MainCalculatorView, Nav

app_name = "calculator"

urlpatterns = [
    path('', CalculatorView.as_view(), name="home"),
    path('home/', MainCalculatorView.as_view(), name="index"),
    path('nav/', Nav.as_view(), name="nav"),
]