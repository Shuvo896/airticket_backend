from django.contrib import admin
from .models import Flight, Booking

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_no', 'origin', 'destination', 'departure_time', 'arrival_time', 'seats_available')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'booking_time', 'status')
    list_filter = ('status',)
