from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('hello/', views.say_hello, name='say_hello')
]