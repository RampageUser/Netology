from .models import Sensor, Measurement
from .serializers import *
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class SensorCorrectView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementAddView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer


# class SensorAllInfoView(RetrieveUpdateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
