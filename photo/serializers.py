from models import Photo
from rest_framework import serializers


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('img_url', 'author')
