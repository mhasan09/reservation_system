from rest_framework import serializers
from .models import *

#Serializer class to retrieve,post and update the Notes data
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RESERVATION
        fields = '__all__'

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = VACANCY
        fields = '__all__'

