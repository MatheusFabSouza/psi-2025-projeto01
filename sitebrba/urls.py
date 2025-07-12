from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("", views.index, name="inicio"),
    path("elenco/", views.elenco, name="elenco"),
    path("sobre/", views.sobre, name="sobre"),
]

