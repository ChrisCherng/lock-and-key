"""
Imports path from django in order to route to the correct templates
Imports the views.py file
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomList.as_view(), name='home'),
    path('contact/', views.ContactPage.as_view(), name='contact_form'),
    path(
        'booking-date/',
        views.BookingPageDate.as_view(),
        name='booking_page_date/'
        ),
    path('booking/', views.BookingPage.as_view(), name='booking_page'),
    path('mybookings/', views.BookingsByUser.as_view(), name='my_bookings'),
    path('signup/', views.signup, name='signup'),
    path('delete/<booking_id>', views.delete_booking, name='delete'),
    path('<slug:slug>/', views.RoomDetail.as_view(), name='room_detail'),
]
