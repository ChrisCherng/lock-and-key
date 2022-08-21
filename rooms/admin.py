from django.contrib import admin
from .models import Room
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('room_description')

