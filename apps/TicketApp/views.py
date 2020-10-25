from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.views.generic import View
from django.urls import reverse_lazy

from TicketManagement import settings
from .forms import SignUpForm


# Create your views here.
from django.contrib.auth.backends import ModelBackend

class LoginView(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
            print(user)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'signUp.html'
