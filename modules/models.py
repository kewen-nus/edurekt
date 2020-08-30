from django.db import models


class Module(models.Model):
    code = models.CharField(primary_key=True, max_length=32, blank=False)
    name = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=False)
    time = models.DateTimeField(blank=True)
