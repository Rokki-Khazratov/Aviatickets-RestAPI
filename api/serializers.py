from rest_framework import serializers
from .models import CLASS_CHOICES, TIME_CHOICES, Race,Airline


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['name']

class RaceSerializer(serializers.ModelSerializer):
    airline = serializers.CharField(source='airline.name')
    source_city = serializers.SerializerMethodField()
    departure_time = serializers.SerializerMethodField()
    arrival_time = serializers.SerializerMethodField()
    destination_city = serializers.SerializerMethodField()
    class_type = serializers.SerializerMethodField()
    # days_left = serializers.ReadOnlyField()

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
            # 'day',
            'days_left',
            'price'
        ]
        # extra_kwargs = {
        #     'day': {'format': '%Y-%m-%d'}
        # }

    def get_source_city(self, obj):
        return obj.source_city.name

    def get_departure_time(self, obj):
        for code, name in TIME_CHOICES:
            if code == obj.departure_time:
                return name
        return None

    def get_arrival_time(self, obj):
        for code, name in TIME_CHOICES:
            if code == obj.arrival_time:
                return name
        return None

    def get_destination_city(self, obj):
        return obj.destination_city.name

    def get_class_type(self, obj):
        for code, name in CLASS_CHOICES:
            if code == obj.class_type:
                return name
        return None



# class PostRaceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Race
#         fields = [
#             'id',
#             'airline',
#             'flight',
#             'source_city',
#             'departure_time',
#             'stops',
#             'arrival_time',
#             'destination_city',
#             'class_type',
#             'duration',
#             # 'day',
#             # 'days_left',
#             'price'
#         ]
