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

""" about us """
urlpatterns += [
    path('about', views.about, name='about')
]


""" about schools """
urlpatterns += [
    path('school/<int:pk>/about', views.about_sch, name='about_sch')
]


""" register school """
urlpatterns += [
    path('school_reg', views.school_reg, name='school_reg')
]
