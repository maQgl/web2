from __future__ import unicode_literals

from django.db import models
from core.models import BaseModel
from core.models import ModelWithGeneric
from client.models import Client


class Event(BaseModel, ModelWithGeneric):
    author = models.ForeignKey(Client)
