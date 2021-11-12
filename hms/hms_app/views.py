from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requests):
    return render(requests , 'admin/index.html')

def room_status(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        
        my_dict = { 
               "clicked" : name,
               }
        return render(requests, 'admin/room_status.html', context=my_dict)
    else:
       
        return render(requests, 'admin/room_status.html')


def room_manage(request):
    return render(request, 'admin/room_manage.html')
