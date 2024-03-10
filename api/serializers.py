from rest_framework import serializers
from .models import Race,Airline


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['name']

class RaceSerializer(serializers.ModelSerializer):
    airline = AirlineSerializer()
    display_days_left = serializers.ReadOnlyField()

    class Meta:
        model = Race
        fields = [
            'id',
            'airline',
            'flight',
            'source_city',
            'departure_time',
            'stops',
            'arrival_time',
            'destination_city',
            'class_type',
            'duration',
            'day',
            'display_days_left',
            'price'
        ]
