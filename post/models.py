from __future__ import unicode_literals

from django.db import models
from client.models import Client
from core.models import BaseModel
from like.models import LikeMixin

class Post(BaseModel, LikeMixin):
    author = models.ForeignKey(Client)
