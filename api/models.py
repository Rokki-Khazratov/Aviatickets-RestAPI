from django.db import models
from django.utils import timezone

TIME_CHOICES = [
    (1, 'Early_morning'),
    (2, 'Morning'),
    (3, 'Day'),
    (4, 'Evening'),
    (5, 'Night'),
    (6, 'Late_Night'),
]

CLASS_CHOICES = [
    (1, 'Econom'),
    (2, 'Business'),
]

class Race(models.Model):
    airline = models.CharField(max_length=100)
    flight = models.CharField(max_length=12)
    source_city = models.CharField(max_length=100)
    departure_time = models.IntegerField(choices=TIME_CHOICES)
    stops = models.PositiveSmallIntegerField(default=0)
    arrival_time = models.IntegerField(choices=TIME_CHOICES)
    destination_city = models.CharField(max_length=100)
    class_type = models.IntegerField(choices=CLASS_CHOICES)
    duration = models.FloatField()
    day = models.DateField()

    @property
    def display_days_left(self):
        today = timezone.now().date()
        remaining_days = (self.day - today).days
        return remaining_days
