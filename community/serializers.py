from models import Community
from rest_framework import serializers


class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Community
        fields = ('admin', 'participants')
