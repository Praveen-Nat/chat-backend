from django.contrib import admin
from django.urls import path, include
from .views import contactPost, contactGet

urlpatterns = [
  
 path('post/', contactPost),
 path('get/', contactGet),
 
  
  
]

