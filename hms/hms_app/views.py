from django.shortcuts import render,redirect
from django.http import HttpResponse
from hms_app.models import Admin, Housekeeper, Room_floor, Room, Room_details, Housekeeper_details, Housekeeper_room_visit

# Create your views here.

def index(requests):
    total_room = Room.objects.all().count()
    cleaned = Room_details.objects.filter(room_inspect_status="Inspected").count()
    dirty = Room_details.objects.filter(room_inspect_status="Dirty").count()
    out_of_serviced = Room_details.objects.filter(room_status="Out-of-Service").count()
    out_of_order = Room_details.objects.filter(room_status="Out-of-Order").count()
    available_room = Room_details.objects.filter(room_occupancy="Vacant").count()
    not_available_room = Room_details.objects.filter(room_occupancy="Occupied").count()
    housekeeper = Housekeeper_details.objects.filter(housekeeper_status="Available").count()
    my_dict={
        
        "total_room": total_room,
        "cleaned": cleaned,
        "dirty": dirty,
        
        "out_of_serviced": out_of_serviced,
        "out_of_order": out_of_order,
        "available_room": available_room,
        "not_available_room": not_available_room,
        "housekeeper": housekeeper,
    }
    
    return render(requests , 'admins/index.html',context=my_dict)

def room_status(requests):
    room_data = Room_details.objects.all()
    my_dict = {            
                "room_data": room_data,                     
            }
    return render(requests, 'admins/room_status.html', context=my_dict)

def room_manage(request):
    if request.method == "POST":
        room_data_id = request.POST.get('room_data_id')
        room_data = Room_details.objects.all().filter(id=room_data_id)
        Housekeeper_data = Housekeeper_details.objects.all().filter(housekeeper_status='Available')
        my_dict = {
            "room_data": room_data,
            "Housekeeper_data": Housekeeper_data,
        }
        return render(request, 'admins/room_manage.html',context=my_dict)

def room_update(request):
    if request.method == "POST":
        room_id = request.POST.get("room_id")
        room_inspection = request.POST.get("room_inspected")
        room_note = request.POST.get("room_note")
        room_status = request.POST.get("room_status")
        housekeeper_id = request.POST.get("housekeeper_id")
        update_data = Room_details.objects.filter(id=room_id).update(
            room_inspect_status=room_inspection, room_notes=room_note, room_housekeeper=housekeeper_id, room_status=room_status)
        update_housekeeper_data = Housekeeper_details.objects.filter(housekeeper_id=housekeeper_id).update(housekeeper_status="Occupied")
        return redirect("/room_status")
