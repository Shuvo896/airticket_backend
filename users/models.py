from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

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
        return f"{self.username} ({self.email})"

    def set_password(self, raw_password):
        self.password = make_password(raw_password)  # Hash password before saving

    def save(self, *args, **kwargs):
        if not self.pk:  # Only hash password on first save (signup)
            self.set_password(self.password)
        super().save(*args, **kwargs)



class PassengerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class Passenger(AbstractBaseUser):
    passport_number = models.CharField(max_length=50, unique=True)
    nationality = models.CharField(max_length=50)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    role = models.CharField(default='passenger', max_length=10, editable=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'passport_number']
    
    objects = PassengerManager()
    
    class Meta:
        verbose_name = 'Passenger'
        verbose_name_plural = 'Passengers'

    def __str__(self):
        return self.email

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


