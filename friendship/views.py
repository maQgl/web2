from django.shortcuts import render
from rest_framework import viewsets
from serializers import FriendshipSerializer
from models import Friendship


class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
