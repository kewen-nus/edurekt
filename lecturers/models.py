from django.db import models

class Lecturer(models.Model):
    name = models.CharField(max_length=256, blank=False)
    department = models.CharField(max_length=256, blank=False)

    def __str__(self):
            return "{}: {}".format(self.name, self.department)