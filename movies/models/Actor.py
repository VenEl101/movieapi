from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name
