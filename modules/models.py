from django.db import models

from rooms.models import Room

from lecturers.models import Lecturer

class Module(models.Model):
    code = models.CharField(primary_key=True, max_length=32, blank=False)
    name = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=True)
    time = models.DateTimeField(blank=True, null=True)

    lecturer = models.ForeignKey(Lecturer, on_delete=models.deletion.SET_NULL, null=True)

    room = models.OneToOneField(Room, on_delete=models.deletion.SET_NULL, null=True)

    def __str__(self):
        return "{}: {}".format(self.code, self.name)
