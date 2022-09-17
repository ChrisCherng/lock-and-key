"""
Imports the admin view from django
Imports the Summernote addin for text fields in admin view
Imports the models
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Room, Booking, ContactInfo


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):
    """ Sets the admin view for the Rooms model """
    list_display = ('title', 'status', )
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('room_description')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Sets the admin view for the Booking model """
    list_display = (
        'room_selected', 'name', 'date_selected',
        'time_selected', 'booking_type',
        )
    list_filter = ('date_selected',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    """ Sets the admin view for the Contact model """
    list_display = (
        'name', 'date_sent',
        )
    list_filter = ('date_sent',)
