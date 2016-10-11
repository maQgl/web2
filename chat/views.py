from django.shortcuts import render
from rest_framework import viewsets
from serializers import ChatSerializer
from models import Chat


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
