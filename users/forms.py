from django import forms
from .models import Passenger
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class PassengerSignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        min_length=8
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )
    
    class Meta:
        model = Passenger
        fields = ['username', 'email', 'password', 'passport_number', 'nationality', 'date_of_birth']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'passport_number': forms.TextInput(attrs={'placeholder': 'Passport Number'}),
            'nationality': forms.TextInput(attrs={'placeholder': 'Nationality'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date of Birth (YYYY-MM-DD)'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Passenger.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords don't match")
        
        return cleaned_data
    
    def save(self, commit=True):
        passenger = super().save(commit=False)
        passenger.password = make_password(self.cleaned_data['password'])
        if commit:
            passenger.save()
        return passenger