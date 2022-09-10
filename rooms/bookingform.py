from django import forms
from .models import Booking, ContactInfo


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('room_selected', 'name', 'email', 'date_selected', 'time_selected',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ('name', 'email', 'message',)