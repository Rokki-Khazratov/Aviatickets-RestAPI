from django.db import models as m
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

STOPS_CHOICES = [
    (0, '0'),
    (1, '1'),
    (2, 'Two and more'),
]

class Airline(m.Model):
    name = m.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class City(m.Model):
    name = m.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Race(m.Model):
    airline = m.ForeignKey(Airline,on_delete=m.CASCADE)
    flight = m.CharField(max_length=12)
    source_city = m.ForeignKey(City,on_delete=m.CASCADE,related_name='source_city')
    departure_time = m.IntegerField(choices=TIME_CHOICES)
    stops = m.IntegerField(choices=STOPS_CHOICES)
    arrival_time = m.IntegerField(choices=TIME_CHOICES)
    destination_city = m.ForeignKey(City,on_delete=m.CASCADE,related_name='destination_city')
    class_type = m.IntegerField(choices=CLASS_CHOICES)
    duration = m.FloatField()
    # day = m.DateField()
    days_left = m.IntegerField()
    price = m.IntegerField(blank=True,null=True)

    # @property
    # def days_left(self):    
    #     today = timezone.now().date()
    #     remaining_days = (self.day - today).days
    #     return remaining_days if remaining_days >= 0 else 0 

    def __str__(self):
        return f"{self.airline} - {self.flight}"