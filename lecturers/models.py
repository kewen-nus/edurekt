from django.db import models

from modules.models import Module


class Lecturer(models.Model):
    name = models.CharField(max_length=256, blank=False)
    department = models.CharField(max_length=128, blank=False)

    module = models.ForeignKey(Module, related_name='lecturers', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)
