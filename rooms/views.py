from django.shortcuts import render
from django.views import generic
# from .models import Room

def RoomList(request):
    # model = Room
    # queryset = Room.objects.filter(status=1)
    return render(request,'index.html')