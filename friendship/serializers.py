from models import Friendship
from rest_framework import serializers


class FriendshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friendship
        fields = ('author', 'participant')
