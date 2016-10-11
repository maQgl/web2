from __future__ import unicode_literals

from django.db import models
from core.models import BaseModel
from client.models import Client


class Community(BaseModel):
    admin = models.ForeignKey(Client, related_name='community_admin')
    particapants = models.ManyToManyField(Client)
