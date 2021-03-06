from django.shortcuts import render
from rest_framework import viewsets
from serializers import PhotoSerializer
from models import Photo


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
