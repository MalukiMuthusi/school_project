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


""" Form to request student's data """


class request_dataForm(forms.Form):
    Admn = forms.IntegerField(
        label="Admission Number",
        max_value=10000,
        min_value=0,
        help_text="Enter students admission number in the school to search",
    )
    school = forms.ModelChoiceField(
        label="Former School",
        help_text="Select Student's Former School",
        queryset=School.objects.all(),
    )
