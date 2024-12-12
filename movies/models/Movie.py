from django.db import models
from .Actor import Actor

class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    imdb = models.FloatField()
    genre = models.CharField(max_length=50)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name



