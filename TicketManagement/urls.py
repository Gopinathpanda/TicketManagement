"""TicketManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from apps.TicketApp.views import SignUpView
from django.views.generic import TemplateView
from apps.TicketApp.forms import CustomAuthForm

urlpatterns = [
    path('', auth_views.LoginView.as_view(form_class=CustomAuthForm), name="home"),
    path("registration/", SignUpView.as_view(), name="register"),
    path('ticket/', TemplateView.as_view(template_name='ticket.html'), name='ticket')
]
