
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from BankClient.views import login,user_dashboard

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', user_dashboard, name='dashboard'),
]
