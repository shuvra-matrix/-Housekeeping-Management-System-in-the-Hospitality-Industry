from django.contrib import admin
from django.urls import path
from hms_app import views

app_name= "hmsapp"

urlpatterns = [
    path('',views.index,name='index'),
    path('room_status/', views.room_status,name="room_status"),
    path('room_manage/',views.room_manage,name="room_manage"),
    path('room_update/',views.room_update,name="room_update"),
    path('housekeepers/', views.housekeepers_manage, name="housekeepers"),
    path('add_housekeeper/',views.add_housekeeper,name="add_housekeeper"),
    path("housekeepers/details", views.housekeeper_details,
         name="housekeeper_details"),
    path("housekeeper_update/", views.housekeeper_update, name="housekeeper_update"),
    path("housekeeper_delete/", views.housekeeper_delete, name="housekeeper_delete"),
    path("rooms_and_floor/", views.rooms_and_floor,name="rooms_and_floor"),
    path("rooms_and_floor/add_room", views.add_room_floor,
         name="add_room"),
    path("rooms_and_floor/add_floor", views.add_room_floor,
         name="add_floor"),
    path("rooms_and_floor/edit_floor", views.add_room_floor,
         name="edit_floor"),
    path("rooms_and_floor/edit_room", views.add_room_floor,
         name="edit_room"),
]
