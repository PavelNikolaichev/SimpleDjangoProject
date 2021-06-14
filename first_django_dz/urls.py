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
    path('', IndexView.as_view()),

    path('riddle/', RiddleView.as_view()),
    path('answer/', AnswerView.as_view()),
    path('multiply/', MultiplyView.as_view()),
    path('expression/', ExpressionView.as_view()),
    path('calculator/', CalculatorView.as_view()),
    path('exphistory/', ExpressionHistoryView.as_view()),
    path('str2words/', StrCountView.as_view()),
    path('str_history/', StrHistoryView.as_view()),
    path('clicker/', ClickerView.as_view()),

    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view())
]
