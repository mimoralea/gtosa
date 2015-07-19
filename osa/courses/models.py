from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    hours = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.code + ": " + self.name
