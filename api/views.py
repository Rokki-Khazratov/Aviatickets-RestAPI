from rest_framework import generics
from .models import Race
# from .serializers import PostRaceSerializer
from .serializers import RaceSerializer
from django.db.models import F, ExpressionWrapper, DateTimeField

from django.utils import timezone



class RaceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class RaceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Race.objects.annotate(
    #     days_left=ExpressionWrapper(
    #         F('day') - timezone.now(),
    #         output_field=DateTimeField()
    #     )
    # )
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

    # def get_queryset(self):
    #     return list(self.queryset.values(*self.serializer_class.Meta.fields, 'days_left'))





# class PostRaceView(generics.CreateAPIView):
#     queryset = Race.objects.all()
#     serializer_class = PostRaceSerializer
#     print(queryset)

    