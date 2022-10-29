from django.urls import path
from .views import CalculatorView, MainCalculatorView

app_name = "calculator"

urlpatterns = [
    path('', CalculatorView.as_view(), name="home"),
    path('home/', MainCalculatorView.as_view(), name="index"),
]