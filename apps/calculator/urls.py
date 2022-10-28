from django.urls import path
from .views import CalculatorView

app_name = "calculator"

urlpatterns = [
    path('', CalculatorView.as_view(), name="home")
]