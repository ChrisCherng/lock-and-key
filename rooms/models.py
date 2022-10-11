"""
Imports the required elements including:
'models' from the django database
'ArrayField' from django/postgres to contain the possible booking times
'CloudinaryField' for the upload of room images to cloudinary
"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Live"))
BOOKING_STATUS = ((0, "Customer Booked"), (1, "Management Blocked"))


class Room(models.Model):
    """
    Data model to contain the information on the different escape rooms.
    Includes possible times for the games that the admin can input and amend.
    Allows admin to draft the info before going live using the 'status' field.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    room_description = models.TextField()
    room_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    times = ArrayField(models.TimeField(blank=True, null=True, auto_now=False))
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Orders the rooms by status
        Brings 'live' rooms to the top,
        'draft' rooms below.
        """
        ordering = ("-status", )

    def __str__(self):
        return self.title


class Booking(models.Model):
    """
    Data model to contain bookings.
    Allows the admin to make 'management blocked' bookings to make slots 
    unavailable using the 'booking_type" field.
    """
    room_selected = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, unique=False)
    email = models.EmailField(max_length=80, unique=False)
    date_selected = models.DateField(blank=True, null=True, auto_now=False)
    time_selected = models.TimeField(blank=True, null=True, auto_now=False)
    booking_type = models.IntegerField(choices=BOOKING_STATUS, default=0)

    class Meta:
        """
        Orders the bookings in the admin panel
        by the booking date then booking time
        """
        ordering = ("date_selected", "time_selected")

    def __str__(self):
        return f"Booking for {self.room_selected} by {self.name}"


class ContactInfo(models.Model):
    """
    Data model to contain the contact requests from users
    """
    name = models.CharField(max_length=80, unique=False)
    email = models.EmailField(max_length=80, unique=False)
    message = models.TextField()
    date_sent = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
