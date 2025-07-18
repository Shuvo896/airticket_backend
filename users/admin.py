from django.contrib import admin
from .models import User, Passenger, Admin
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'role')
    
@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('user', 'passport_number', 'nationality', 'date_of_birth')
    
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('user', 'staff_id', 'department')