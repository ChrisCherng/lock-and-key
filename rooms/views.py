from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Room, Booking


class RoomList(generic.ListView):
    model = Room
    queryset = Room.objects.filter(status=1)
    template_name = 'index.html'


class RoomDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Room.objects.filter(status=1)
        room = get_object_or_404(queryset, slug=slug)
        return render(
            request, 'room_detail.html', {
                "room": room
            },
        )


def ContactForm(request):
    return render(request,'contact.html')


class BookingPage(generic.ListView):
    model = Room
    queryset = Room.objects.filter(status=1)
    template_name = 'booking.html'
