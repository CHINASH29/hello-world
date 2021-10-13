from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login_info_admin/', views.login_info_admin, name='login_info_admin'),
]
