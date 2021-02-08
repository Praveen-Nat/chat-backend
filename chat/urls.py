from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('<str:room_name>/', views.room, name='room'),
  path('getChat/<str:room>/', views.chatGet )
   
]
