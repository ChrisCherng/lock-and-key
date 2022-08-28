from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Live"))
BOOKING_STATUS = ((0, "Customer Booked"), (1, "Management Blocked"))

class Room(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    room_description = models.TextField()
    room_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    times = ArrayField(models.TimeField(blank=True, null=True, auto_now=False))
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title


class Booking(models.Model):
    room_selected = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, unique=False)
    email = models.EmailField(max_length=80, unique=False)
    date_selected = models.DateField(blank=True, null=True, auto_now=False)
    time_selected = models.TimeField(blank=True, null=True, auto_now=False)
    booking_type = models.IntegerField(choices=BOOKING_STATUS, default=0)

    def __str__(self):
        return f"Booking for {self.room_selected} by {self.name}"
