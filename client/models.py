from __future__ import unicode_literals

from django.db import models
from core.models import BaseModel


class Client(BaseModel):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthdate = models.DateField()
    description = models.TextField()
