from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requests):
    return render(requests , 'admin/index.html')

def room_status(requests):
    return render(requests, 'admin/room_status.html')