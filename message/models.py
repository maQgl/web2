from __future__ import unicode_literals

from django.db import models
from core.models import BaseModel
from chat.models import Chat
from client.models import Client


class Message(BaseModel):
    chat = models.ForeignKey(Client)
    text = models.TextField()
