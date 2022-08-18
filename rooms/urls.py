from . import views
from django.urls import path

urlpatterns = [
    path('', views.RoomList, name='home'),
    path('contact', views.ContactForm, name='contact_form')
]