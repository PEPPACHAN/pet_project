from rest_framework import serializers
from .models import *


class RegistrationAPI(serializers.ModelSerializer):
    class Meta:
        model = Registered_Users
        fields = ["username", "password"]
