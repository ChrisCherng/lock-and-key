"""
Imports the relevant django functions and models
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Room, Booking
from .bookingform import BookingForm



class RoomList(generic.ListView):
    """
    Renders all live rooms onto the hompage
    """
    model = Room
    queryset = Room.objects.filter(status=1)
    template_name = 'index.html'

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.all()
    template_name = 'booking.html'


class RoomDetail(View):
    """
    Renders the full information for each room
    on a separate page
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Gets information on rooms from database
        """
        queryset = Room.objects.filter(status=1)
        room = get_object_or_404(queryset, slug=slug)
        return render(
            request, 'room_detail.html', {
                "room": room
            },
        )


def ContactForm(request):
    """
    Renders the contact form page
    """
    return render(request, 'contact.html')


class BookingPage(generic.ListView):
    """
    Renders the booking form page
    """
    context_object_name = "data"
    #model = Room
    #queryset = Room.objects.filter(status=1)
    template_name = 'booking.html'   

    def get_queryset(self):
        myset = {
            "rooms": Room.objects.all(),
            "bookings": Booking.objects.all(),
        }
        return myset

    def post(self, request, *args, **kwargs):
        """
        Posts user booking to the database
        """
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


class BookingPageDate(generic.ListView):
    context_object_name = "data"
    template_name = 'booking-date.html'

    def get_queryset(self):
        myset = {
            "rooms": Room.objects.all(),
            "bookings": Booking.objects.all(),
        }
        return myset

    def post(self, request, *args, **kwargs):
        """
        Returns main booking form
        """
        date_picked = request.POST['date_selected']
        context = {'date_picked': date_picked, "rooms": Room.objects.all(), "bookings": Booking.objects.all()}
        return render(request, 'booking.html', context)


class BookingConfirmation(View):
    """
    Renders the booking confirmation upon successful booking
    """
    template_name = 'booking-confirmation.html'
