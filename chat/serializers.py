from models import Chat
from rest_framework import serializers


class ChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chat
        fields = ('clients')
