""" Import forms from django and relevant models """
from django import forms
from .models import Booking, ContactInfo


class BookingForm(forms.ModelForm):
    """ Booking form django class to post to database """
    class Meta:
        """ Sets fields for booking form """
        model = Booking
        fields = (
            'room_selected', 'name', 'email', 'date_selected', 'time_selected',
            )


class ContactForm(forms.ModelForm):
    """ Contact form django class to post to database """
    class Meta:
        """ Sets fields for contact form """
        model = ContactInfo
        fields = ('name', 'email', 'message',)
