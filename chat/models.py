from __future__ import unicode_literals

from django.db import models
from core.models import BaseModel
from client.models import Client


class Chat(BaseModel):
    clients = models.ManyToManyField(Client)
