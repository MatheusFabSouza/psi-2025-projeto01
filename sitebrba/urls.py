from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("", views.index, name="inicio"),
    path("elenco/", views.elenco, name="elenco"),
    path("sobre/", views.sobre, name="sobre"),
]

