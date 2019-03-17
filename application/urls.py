from django.urls import path

from . import views

# Function Views

""" Index page view url """
urlpatterns = [
    path('', views.index, name='index')
]
