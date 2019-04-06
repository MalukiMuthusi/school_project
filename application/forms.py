from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Parent, School

# from django.core.exceptions import ValidationError
# from django.contrib.auth.tokens import default_token_generator


class SchoolRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


""" School Form """


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = "__all__"


""" Parent Form """


class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"
