from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name = 'index'),#home a bos adres gelirse viewsteki index methoduna yönlendir
]