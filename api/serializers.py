from rest_framework import serializers
from .models import Race

class RaceSerializer(serializers.ModelSerializer):
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
