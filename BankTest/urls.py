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
from django.urls import path,include
from TestBank.views import register_client,home,view_clients,user_login



urlpatterns = [
    path('TestBank/',include('TestBank.urls')),
    path('', user_login, name='login'),
    path('home', home, name='home'),
    path('register_client/', register_client, name='register_client'),
    path('view_clients/', view_clients, name='view_clients'),
    path('login/', user_login, name='login'),
    ]

