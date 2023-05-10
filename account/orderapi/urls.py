from django.urls import path
from . import views

urlpatterns = [
    path('orderapi/', views.getData),
    path('take/', views.takeOrder)
]