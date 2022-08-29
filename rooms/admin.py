from django.contrib import admin
from .models import Room, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', )
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('room_description')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('room_selected', 'name', 'date_selected', 'time_selected', 'booking_type',)

