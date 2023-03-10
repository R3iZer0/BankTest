"""BankTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView, LogoutView

from TestBank.views import client_login, client_register,home,view_clients,user_login,dashboard,edit_client,delete_client,client_dashboard



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('home/', home, name='home'),
    path('dashboard/',dashboard, name='dashboard'),  # new URL pattern
    path('register_client/', client_register, name='register_client'),
    path('view_clients/', view_clients, name='view_clients'),
    path('edit_client/<int:pk>/', edit_client, name='edit_client'),
    path('delete_client/<int:client_id>/',delete_client, name='delete_client'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('client_login/',client_login, name='client_login'),
    path('client_dashboard/', client_dashboard, name='client_dashboard'),

    ]

