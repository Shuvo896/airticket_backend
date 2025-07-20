from django.contrib import admin
from .models import Passenger, Admin
# from .models import User, Passenger, Admin
# Register your models here.


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('passport_number', 'nationality', 'username', 'email', 'date_of_birth')
    search_fields = ('username', 'email', 'passport_number', 'nationality')
    list_filter = ('nationality',)

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'name', 'department', 'email')
    search_fields = ('staff_id', 'name', 'email', 'department')
    list_filter = ('department',)



# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'username', 'email', 'role')
    
# @admin.register(Passenger)
# class PassengerAdmin(admin.ModelAdmin):
#     list_display = ('user', 'passport_number', 'nationality', 'date_of_birth')
    
# @admin.register(Admin)
# class AdminAdmin(admin.ModelAdmin):
#     list_display = ('user', 'staff_id', 'department')