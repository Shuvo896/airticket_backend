from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PassengerSignupForm

def signup(request):
    if request.method == 'POST':
        form = PassengerSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('home')  # Change to your login route if needed
    else:
        form = PassengerSignupForm()
    
    return render(request, 'users/signup.html', {'form': form})