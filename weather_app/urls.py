from django.urls import path
from weather_app.views import *

urlpatterns = [
    path('', Index, name='index')
]
