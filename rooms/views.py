"""
Imports the relevant django functions and models
"""
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Room, Booking, ContactInfo
from .bookingform import BookingForm, ContactForm


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


class BookingPage(generic.ListView):
    """
    Renders the booking form page
    """
    context_object_name = "data"
    template_name = 'booking.html'


class BookingPageDate(generic.ListView):
    """
    Renders the page to select a booking date
    Passes the booking date to the main booking page    
    """
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
        If the form is submitting the date, passes the date to the next page
        If the form is submitting the booking, posts info to the database
        """
        if 'booking-date-submit' in request.POST:
            date_picked = request.POST[
                'date_selected'
                ]
            context = {
                'date_picked': date_picked,
                "rooms": Room.objects.filter(status=1),
                "bookings": Booking.objects.filter(date_selected=date_picked)
                }
            return render(request, 'booking.html', context)
        elif 'booking-submit' in request.POST:
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
    """
    Renders the booking confirmation upon successful booking
    """
    template_name = 'booking-confirmation.html'


class ContactPage(generic.ListView):
    """
    Renders the contact form page
    """
    model = ContactInfo
    queryset = ContactInfo.objects.all()
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        """
        Posts the booking information to the database
        """
        contact_form = ContactForm(data=request.POST)
        contact_form.name = request.POST.get('name')
        contact_form.email = request.POST.get('email')
        contact_form.message = request.POST.get('message')
        if contact_form.is_valid():
            contact_form.save()
        return render(request, 'contact.html',)
