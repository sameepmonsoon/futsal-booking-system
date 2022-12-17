# from pyexpat import model
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registrationform(UserCreationForm):
    email = forms.Emailfield()

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]