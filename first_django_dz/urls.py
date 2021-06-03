"""first_django_dz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path

from landing.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('riddle/', riddle),
    path('answer/', answer),
    path('multiply/', multiply),
    path('expression/', expression),
    path('calculator/', calculator),
    path('exphistory/', exp_history),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('str2words/', strCount),
    path('str_history/', str_history),
    path('clicker/', Clicker)
]
