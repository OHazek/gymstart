"""Apka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from Cwiczenia.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name ='index'),
    path('partie/<id>/', partia, name='partia'),
    path('cwiczenie/<id>/', cwiczenie, name='cwiczenie'),
    path('kalkulator/', kalkulator, name='kalkulator'),
    path('plan/', plan, name='plan'),
    path('rejestracja/', rejestracja, name='rejestracja'),
    path('logowanie/', logowanie, name='logowanie'),
    path('wylogowanie/', wylogowanie, name='wylogowanie'),
    path('progres/', progres, name='progres'),
    path('rekordy/', rekordy, name='rekordy'),
    path('rekordy/rekord/<id>/', rekord, name='rekord'),

]
