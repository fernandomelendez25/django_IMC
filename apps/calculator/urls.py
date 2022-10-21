from django.urls import path
from .views import CalculateView

app_name = "calculator"

urlpatterns = [
    path('', CalculateView.as_view(), name="home")
]