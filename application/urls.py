from django.urls import path

from . import views

# Function Views

""" Index page view url """
urlpatterns = [
    path('', views.index, name='index')
]

""" Add the school view absolute url """
urlpatterns += [
    path('school/<int:pk>', views.school, name='school')
    ]

""" List all schools """
urlpatterns += [
    path('all_schools', views.all_schools, name='all_schools')
]
