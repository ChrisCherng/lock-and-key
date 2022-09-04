from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Room, Booking
from .bookingform import BookingForm


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

    def post(self, request, *args, **kwargs):

        booking_form = BookingForm(data=request.POST)
        booking_form.room_selected = request.POST.get('room_selected')
        booking_form.name = request.POST.get('name')
        booking_form.email = request.POST.get('email')
        booking_form.date_selected = request.POST.get('date_selected')
        booking_form.time_selected = request.POST.get('time_selected')
        if booking_form.is_valid():
            booking_form.save()
            return render(request, 'booking-confirmation.html',)
        else:
            return render(request, 'booking.html',)

      
class BookingConfirmation(View):
    template_name = 'booking-confirmation.html'