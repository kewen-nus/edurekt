from django.db import models


class Student(models.Model):
    matric_number = models.CharField(primary_key=True, max_length=9, blank=False)
    name = models.CharField(max_length=256, blank=False)
    year = models.PositiveSmallIntegerField(blank=False, default=1)
    course = models.CharField(max_length=256, blank=False)
