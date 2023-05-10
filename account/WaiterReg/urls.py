from django.contrib import admin
from . import views 
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='waiter-home'),
    path('restaurant_list/', views.restaurant_list, name='restaurant_list'),
]