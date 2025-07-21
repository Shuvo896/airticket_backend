from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

from django.db import models
from django.contrib.auth.models import User

class Passenger(models.Model):
    passport_number = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=128)
    role = models.CharField(default='passenger', max_length=10, editable=False)

    class Meta:
        unique_together = ('passport_number', 'nationality')
        verbose_name = 'Passenger'
        verbose_name_plural = 'Passengers'

    def __str__(self):
        return f"{self.username} ({self.passport_number}, {self.nationality})"
    
class Admin(models.Model):
    staff_id = models.CharField(max_length=50, primary_key=True)
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(default='admin', max_length=10, editable=False)

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def __str__(self):
        return f"{self.name} ({self.staff_id})"


