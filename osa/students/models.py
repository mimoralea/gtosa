from django.db import models


class Student(models.Model):
    display_name = models.CharField(max_length=50)

    def __str__(self):
        return self.display_name
