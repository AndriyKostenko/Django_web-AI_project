from django.urls import path

from .views import *
from .video_services import get_streaming_video


urlpatterns = [
    path('', base, name='base'),
    path('play/', play, name='play'),
    path('watch/', watch, name='watch'),
    path('stream/<int:pk>/', get_streaming_video, name='stream'),
    path('recognize/', recognize, name='recognize'),
    path('weather/', weather, name='weather'),
    path('location/', location, name='location'),
]