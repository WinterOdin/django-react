from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_pause',
                  'votes', 'created')


class  CreateRoom(serializers.ModelSerializer):
    class Meta:
        model  = Room
        fields = ('guest_pause', 'votes') 