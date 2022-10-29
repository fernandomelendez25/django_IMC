from django.urls import path
from .views import CalculatorView, MainCalculatorView, SignUpView

app_name = "calculator"

urlpatterns = [
    path('', CalculatorView.as_view(), name="home"),
    path('home/', MainCalculatorView.as_view(), name="index"),
    path('signup/', SignUpView.as_view(), name="signup"),
]