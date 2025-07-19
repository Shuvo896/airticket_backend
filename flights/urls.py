from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('home/', views.home, name='home'),
]