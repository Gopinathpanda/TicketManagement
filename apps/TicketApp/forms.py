from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Email'}), label='')
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}), label='')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length= 254, help_text='Enter a valid email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', ]
