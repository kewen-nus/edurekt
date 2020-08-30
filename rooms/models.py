from django.db import models


class Room(models.Model):
    code = models.CharField(primary_key=True, max_length=32, blank=False)
    name = models.CharField(max_length=256, blank=False)
    address = models.CharField(max_length=256, blank=False)
    max_cap = models.PositiveSmallIntegerField(blank=False)