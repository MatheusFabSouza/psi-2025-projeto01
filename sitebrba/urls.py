from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sitebrba.urls')), 
]

