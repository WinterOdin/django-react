from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from .serializers import *
from .models import *


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer




class GetRoom(APIView):
    serializer_class = RoomSerializer
    lookup_url_kwarg = 'code'

    def get(self,request, format=None):
        code = request.GET.get(self.lookup_url_kwarg)
        if code != None:
            room = Room.objects.filter(code=code)
            if len(room) > 0:
                data = RoomSerializer(room[0]).data
                data['host'] = self.request.session.session_key == room[0].host
                return Response(data,status=status.HTTP_200_OK)
            return Response("No room found", status=status.HTTP_404_NOT_FOUND)
        return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)




class CreateRoom(APIView):
    serializer_class = CreateRoom

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_pause = serializer.data.get("guest_pause")
            votes       = serializer.data.get("votes")
            host        = self.request.session.session_key
            queryset    = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_pause = guest_pause
                room.votes       = votes
                room.save(update_fields=['guest_pause','votes'])
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                room = Room(host=host,guest_pause=guest_pause,votes=votes)
                room.save()
                return Response(RoomSerializer(room).data,status.HTTP_201_CREATED)

        return Response({"Bad request"},status=status.HTTP_400_BAD_REQUEST)
            
            
