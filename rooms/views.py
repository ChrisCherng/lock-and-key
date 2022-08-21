from django.shortcuts import render
from django.views import generic
from .models import Room

class RoomList(generic.ListView):
    model = Room
    queryset = Room.objects.filter(status=1)
    template_name = 'index.html'

def ContactForm(request):
    return render(request,'contact.html')

def BookingPage(request):
    return render(request,'booking.html')