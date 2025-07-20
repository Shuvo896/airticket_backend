from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_no = models.CharField(max_length=10, unique=True, null=True, blank=True)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats_available = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Flights"
        ordering = ['departure_time']
        
    def __str__(self):
        return f"{self.flight_no} - {self.origin} to {self.destination}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    
    class Meta:
        verbose_name_plural = "Bookings"
        ordering = ['-booking_time']
        
    def __str__(self):
        return f"Booking #{self.id} by {self.user.username}"















# class Airport(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     code = models.CharField(max_length=10, unique=True)  # e.g. DAC for Dhaka

#     def __str__(self):
#         return f"{self.city} ({self.code})"

# class Airline(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=10, unique=True)  # e.g. BG for Biman

#     def __str__(self):
#         return self.name

# class Flight(models.Model):
#     airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
#     flight_number = models.CharField(max_length=20)
#     source = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
#     destination = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
#     departure_time = models.DateTimeField()
#     arrival_time = models.DateTimeField()
#     duration = models.DurationField()
#     seats_available = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.flight_number} | {self.source.code} → {self.destination.code}"


# class SearchHistory(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     source = models.ForeignKey(Airport, related_name='search_source', on_delete=models.CASCADE)
#     destination = models.ForeignKey(Airport, related_name='search_destination', on_delete=models.CASCADE)
#     date = models.DateField()
#     searched_at = models.DateTimeField(auto_now_add=True)

# class Booking(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     booked_at = models.DateTimeField(auto_now_add=True)
#     passenger_name = models.CharField(max_length=100)
#     seat_number = models.CharField(max_length=10)
#     status = models.CharField(max_length=20, choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])
