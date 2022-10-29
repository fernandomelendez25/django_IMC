from django.urls import path
from .views import CalculatorView, MainCalculatorView, SignUpView, DiagnosticoListView

app_name = "calculator"

urlpatterns = [
    path('', CalculatorView.as_view(), name="home"),
    path('home/', MainCalculatorView.as_view(), name="index"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('diagnosticos/', DiagnosticoListView.as_view(), name="diagnosticos"),
]