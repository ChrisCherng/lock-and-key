from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Room


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

def BookingPage(request):
    return render(request,'booking.html')