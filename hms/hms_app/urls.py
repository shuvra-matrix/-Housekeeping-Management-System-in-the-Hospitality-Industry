from django.contrib import admin
from django.urls import path
from hms_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('room_status/', views.room_status,name="room_status"),
]
