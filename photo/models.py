from __future__ import unicode_literals

from django.db import models
from core.models import BaseModel
from client.models import Client
from like.models import LikeMixin


class Photo(Client, LikeMixin):
    img_url = models.TextField()
    author = models.ForeignKey(Client, related_name='photo_author')
