from rest_framework import generics
from .models import Race
from .serializers import RaceSerializer

class RaceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class RaceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer