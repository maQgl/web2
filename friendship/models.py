from __future__ import unicode_literals

from django.db import models
from core.models import BaseModel
from client.models import Client


class Friendship(BaseModel):
    author = models.ForeignKey(Client, related_name='friendship_author')
    participant = models.ForeignKey(Client, related_name='friendship_paricipant')
