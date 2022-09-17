"""
Imports path from django in order to route to the correct templates
Imports the views.py file
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomList.as_view(), name='home'),
    path('<slug:slug>/', views.RoomDetail.as_view(), name='room_detail'),
    path('contact', views.ContactPage.as_view(), name='contact_form'),
    path(
        'booking-date',
        views.BookingPageDate.as_view(),
        name='booking_page_date'
        ),
    path('booking', views.BookingPage.as_view(), name='booking_page')
]
