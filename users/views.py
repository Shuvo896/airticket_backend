from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PassengerSignupForm, PassengerLoginForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST':
        form = PassengerSignupForm(request.POST)
        if form.is_valid():
            # Save the passenger with hashed password
            passenger = form.save()
            
            # Optional: Log the user in immediately after registration
            # You'll need to implement an authentication backend for Passenger model
            # login(request, passenger)  
            
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('home')  # Change to your desired redirect page
        else:
            # Form is invalid - errors will be displayed in template
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PassengerSignupForm()
    
    return render(request, 'users/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = PassengerLoginForm(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
    else:
        form = PassengerLoginForm()
    
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')