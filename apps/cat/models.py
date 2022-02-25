from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
