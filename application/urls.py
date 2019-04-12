from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

# Function Views

""" Index page view url """
urlpatterns = [path("", views.index, name="index")]

""" Add the school view absolute url """
urlpatterns += [path("school/<int:pk>", views.school, name="school")]

""" List all schools """
urlpatterns += [path("all_schools", views.all_schools, name="all_schools")]


""" about us and about schools """
urlpatterns += [
    path("about", views.about, name="about"),
    path("school/<int:pk>/about", views.about_sch, name="about_sch"),
]


""" register school """
urlpatterns += [path("school_reg", views.register, name="school_reg")]


""" school admin log in and log out """
urlpatterns += [
    path(
        "school_login",
        auth_views.LoginView.as_view(template_name="school_login.html"),
        name="school_login",
    ),
    path(
        "school_logout",
        auth_views.LogoutView.as_view(template_name="school_logout.html"),
        name="school_logout",
    ),
]


""" school login redirect """
urlpatterns += [path("login_redirect", views.login_redirect, name="login_redirect")]


""" url for client's login and logout """
urlpatterns += [
    path(
        "login", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path(
        "login",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
]
