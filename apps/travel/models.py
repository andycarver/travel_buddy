from __future__ import unicode_literals
from ..login.models import User
from django.db import models

# Create your models here.
class Travel(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    travel_date_from = models.DateField()
    travel_date_to = models.DateField()
    users = models.ManyToManyField(User, related_name='travels')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)