from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('passenger', 'Passenger')])
    
    def __str__(self):
        return self.username

class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='passenger_profile')
    passport_number = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return f"{self.user.username} - {self.passport_number}"

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    staff_id = models.CharField(max_length=50)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.staff_id}"
    