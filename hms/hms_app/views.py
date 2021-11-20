from django.shortcuts import render
from django.http import HttpResponse
from hms_app.models import Admin, Housekeeper, Room_floor, Room, Room_details, Housekeeper_details, Housekeeper_room_visit

# Create your views here.

def index(requests):
    return render(requests , 'admins/index.html')

def room_status(requests):
    floor_data = Room_floor.objects.all()
    for i in floor_data:
        room_name_data = Room.objects.all().filter(floor_id=i.floor_id)
        for j in room_name_data:
            room_data = Room_details.objects.all().filter(room_id=j.room_id)
            if requests.method == 'POST':
                name = requests.POST.get('name')
                                
                my_dict = { 
                    
                                    "floor_data" :floor_data,
                                    "room_data":room_data,
                                    "room_name_data":room_name_data,    
                                    "clicked" : name,
                                    }
                return render(requests, 'admins/room_status.html', context=my_dict)
            else:
                my_dict = {
                                    "floor_data": floor_data,
                                    "room_data": room_data,
                                    "room_name_data": room_name_data,
                                }
                return render(requests, 'admins/room_status.html', context=my_dict)


def room_manage(request):
    return render(request, 'admins/room_manage.html')
