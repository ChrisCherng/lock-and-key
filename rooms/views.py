"""
Imports the relevant django functions and models
"""
from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from .models import Room, Booking, ContactInfo
from .forms import BookingForm, ContactForm, SignUpForm


class RoomList(generic.ListView):
    """
    Renders all live rooms onto the homepage
    """
    model = Room
    queryset = Room.objects.filter(status=1)
    template_name = 'index.html'


class BookingList(generic.ListView):
    """ Renders the booking form """
    model = Booking
    queryset = Booking.objects.all()
    template_name = 'booking.html'


class RoomDetail(View):
    """
    Renders the full information for each room
    on a separate page
    """
    def get(self, request, slug):
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


class BookingPage(LoginRequiredMixin, generic.ListView):
    """
    Renders the booking form page
    """
    context_object_name = "data"
    template_name = 'booking.html'


class BookingPageDate(LoginRequiredMixin, generic.ListView):
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

    def post(self, request):
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


class BookingConfirmation(LoginRequiredMixin, View):
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

    def post(self, request):
        """
        Posts the contact request information to the database
        """
        contact_form = ContactForm(data=request.POST)
        contact_form.name = request.POST.get('name')
        contact_form.email = request.POST.get('email')
        contact_form.message = request.POST.get('message')
        if contact_form.is_valid():
            contact_form.save()
            return render(request, 'contact-confirmation.html',)
        return render(request, 'contact.html',)


class ContactConfirmation(View):
    """
    Renders the contact confirmation upon successful completion of the form
    """
    template_name = 'contact-confirmation.html'


class BookingsByUser(LoginRequiredMixin, generic.ListView):
    """ Renders a list of bookings made by the user if they are logged in """
    model = Booking
    template_name = 'user-bookings.html'
    paginate_by = 10
    today = date.today()

    def get_queryset(self):
        return Booking.objects.filter(
            booking_type=0
            ).filter(
                email=self.request.user.email
                ).filter(
                    date_selected__gt=date.today()
                    ).order_by('date_selected')


def signup(request):
    """ Posts the registration infromation to the database """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def delete_booking(request, booking_id):
    """ deletes the selected booking from the database """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return render(request, 'delete-booking-confirmation.html',)


def amend_booking(request, booking_id):
    """ Renders the amend booking time page """
    booking = get_object_or_404(Booking, id=booking_id)
    context = {
        'booking': booking,
        'bookings': Booking.objects.filter(
            date_selected=booking.date_selected
            ).filter(
                room_selected=booking.room_selected),
    }

    return render(request, 'amend-booking.html', context)


def amend_booking_time(request, booking_id):
    """ Updates the timing of selected booking in the database """
    new_time = request.POST['time_selected']
    booking = Booking.objects.get(id=booking_id)
    booking.time_selected = new_time
    booking.save()
    return render(request, 'amend-booking-time-confirmation.html',)
