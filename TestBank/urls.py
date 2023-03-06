
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, register_client, view_clients,user_login,dashboard

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('home/', home, name='home'),
    path('dashboard/',dashboard, name='dashboard'),  # new URL pattern
    path('register_client/', register_client, name='register_client'),
    path('view_clients/', view_clients, name='view_clients'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', user_login, name='user_login'),
]