from django.shortcuts import render
from .models import User, Passenger, Admin

# Create your views here.

def say_hello(request):
    users = User.objects.all()
    return render(request, 'users/index.html', {'users': users, 'name': 'Bookinfly'})
