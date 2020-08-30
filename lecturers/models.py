from django.db import models


class Lecturer(models.Model):
    name = models.CharField(max_length=256, blank=False)
    department = models.CharField(max_length=128, blank=False)
