from django.shortcuts import render
from django.http import HttpResponse
from hms_app.models import Admin, Housekeeper, Room_floor, Room, Room_details, Housekeeper_details, Housekeeper_room_visit

# Create your views here.

def index(requests):
    return render(requests , 'admins/index.html')

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
