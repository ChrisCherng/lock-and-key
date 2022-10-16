""" Import forms from django and relevant models """
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, help_text='Required')
    last_name = forms.CharField(max_length=50, help_text='Required')
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
