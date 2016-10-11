from __future__ import unicode_literals

from django.db import models
from core.models import BaseModel
from core.models import ModelWithGeneric
from client.models import Client
from like.models import LikeMixin


class Comment(BaseModel, ModelWithGeneric, LikeMixin):
    author = models.ForeignKey(Client)
    text = models.TextField()
