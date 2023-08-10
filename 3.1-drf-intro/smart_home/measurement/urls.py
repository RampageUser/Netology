from django.urls import path
from .views import *

urlpatterns = [
    path('sensors/', SensorsView.as_view()),# get and create sensors
    path('sensors/<pk>/', SensorCorrectView.as_view()),# update and get info about sensor
    path('measurements/', MeasurementAddView.as_view()),# add changes
]
