from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('room_selected', 'name', 'email', 'date_selected', 'time_selected',)

