from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("",         views.inicio, name="index"),
    path("elenco/",  views.elenco,  name="elenco"),
    path("sobre/",   views.sobre,   name="sobre"),
]
