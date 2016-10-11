from django.shortcuts import render
from rest_framework import viewsets
from serializers import LikeSerializer
from models import Like


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
