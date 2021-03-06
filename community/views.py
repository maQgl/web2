from django.shortcuts import render
from rest_framework import viewsets
from serializers import CommunitySerializer
from models import Community


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
