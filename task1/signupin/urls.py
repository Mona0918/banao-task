from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views

app_name='signupin'

urlpatterns = [
    path("",views.homepage,name='homepage'),
    path("usertype/",views.usertyperview,name="usertype"),
    path("signup/",views.registerview,name='signup'),
    path("signin/",views.login,name='signin'),
    #path("signin/",authentication_views.LoginView.as_view(template_name='signin.html'), name="signin"),
    #path("logout/",authentication_views.LogoutView.as_view(template_name='typeofusers.html'),name="logout"),
    path("welcome/<str:name>/",views.homeview,name='welcome'),
    path("logout/",views.logoutview,name='logout'),
]