from django.shortcuts import render

from application.models import Parent, School, Student


# Create your views here.
def index(request):
    return render(request, 'base_generic')
