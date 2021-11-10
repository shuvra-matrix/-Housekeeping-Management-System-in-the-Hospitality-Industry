from django.contrib import admin
from django.urls import path
from hms_app import views

app_name= "hmsapp"

urlpatterns = [
    path('',views.index,name='index'),
    path('room_status/', views.room_status,name="room_status"),
    path('room_manage/',views.room_manage,name="room_manage"),
]
