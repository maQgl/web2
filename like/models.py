from __future__ import unicode_literals

from django.db import models
from core.models import BaseModel
from core.models import ModelWithGeneric
from client.models import Client
from django.contrib.contenttypes.fields import GenericRelation


class Like(BaseModel, ModelWithGeneric):
    author = models.ForeignKey(Client)


class LikeMixin(models.Model):
    likes = GenericRelation(Like, content_type_field='item_type',
                            object_id_field='item_id')
    likes_count = models.PositiveIntegerField(default=1)

    class Meta:
        abstract = True
