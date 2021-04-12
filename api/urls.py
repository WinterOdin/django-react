from django.urls import path
from .views import *

urlpatterns = [
    path('room', RoomView.as_view()),
    path('create', CreateRoom.as_view(),),
    path('get-info', GetRoom.as_view(),)
    path('join-room', JoinRoom.as_view())
]