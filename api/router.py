from django.urls import path
from .views import *

urlpatterns = [
    path('races/', RaceListCreateAPIView.as_view(), name='race-list-create'),
    path('races/<int:pk>/', RaceRetrieveUpdateDestroyAPIView.as_view(), name='race-retrieve-update-destroy'),
    path('predict-race/<int:pk>/', PredictRaceView.as_view(), name='predict-race'),
    # path('predict-race/', PostRaceView.as_view(), name='predict-race')
]
