from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Flight, Booking

def home(request):
    if request.method == 'GET':
        flights = Flight.objects.all().order_by('departure_time')[:5]
        return render(request, 'flights/home.html', {'flights': flights})
    return redirect('home')

def search_flights(request):
    if request.method == 'GET':
        origin = request.GET.get('origin', '').strip()
        destination = request.GET.get('destination', '').strip()
        date = request.GET.get('date', '').strip()
        
        if not (origin and destination):
            messages.warning(request, 'Please enter both origin and destination')
            return redirect('home')
            
        flights = Flight.objects.filter(
            origin__icontains=origin,
            destination__icontains=destination
        )
        
        if date:
            flights = flights.filter(departure_time__date=date)
            
        return render(request, 'flights/search_results.html', {
            'flights': flights,
            'origin': origin,
            'destination': destination,
            'date': date
        })
    return redirect('home')

@login_required
@transaction.atomic
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    
    if flight.seats_available <= 0:
        messages.error(request, 'No seats available for this flight')
        return redirect('search_flights')
        
    Booking.objects.create(user=request.user, flight=flight)
    flight.seats_available -= 1
    flight.save()
    
    messages.success(request, 'Booking confirmed successfully!')
    return render(request, 'flights/booking_success.html', {'flight': flight})