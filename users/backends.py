from .models import Passenger
from django.contrib.auth.backends import BaseBackend

class PassengerAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            passenger = Passenger.objects.get(email=email)
            if passenger.check_password(password):
                return passenger
        except Passenger.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Passenger.objects.get(pk=user_id)
        except Passenger.DoesNotExist:
            return None