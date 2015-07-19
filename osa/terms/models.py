from django.db import models


class Term(models.Model):
    NAME_CHOICES = (
        ('S', 'SPRING'),
        ('M', 'SUMMER'),
        ('F', 'FALL'),
    )
    name = models.CharField(max_length=1, choices=NAME_CHOICES)
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.NAME_CHOICES[self.name] + str(self.year)
