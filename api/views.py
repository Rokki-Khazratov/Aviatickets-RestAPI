from rest_framework import generics
from .models import Race
from .prediction import PredictRaceSerializer
from .serializers import RaceSerializer
from rest_framework.response import Response
from rest_framework import generics

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import pickle




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




try:
    with open('materials/model.pkl', 'rb') as f:
        data = pickle.load(f)
except Exception as e:
    print("Ошибка загрузки модели:", e)

class PredictRaceView(generics.RetrieveAPIView):
    queryset = Race.objects.all()
    serializer_class = PredictRaceSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        serialized_data = serializer.data
        df = pd.DataFrame(serialized_data)
        num = ["duration", "days_left"]
        cat = ['airline', 'source_city', 'departure_time', 'stops',
               'arrival_time', 'destination_city', 'class_type']
    
        num_pipeline = Pipeline([('std_scaler', StandardScaler())])
        full_pipeline = ColumnTransformer([
            ('num_pipe', num_pipeline, num),
            ('cat', OneHotEncoder(), cat)])
        p_data = full_pipeline.fit_transform(df)
        print(full_pipeline)
        
        try:
            result = data.predict(p_data)
        except Exception as e:
            # print("Error:", e)
            result = None

        # Loop over result if it's not None
        # if result is not None:
        #     for i in result:
        #         print(i)
        # else:
        #     print("loop else")
        
        return Response(serialized_data)

