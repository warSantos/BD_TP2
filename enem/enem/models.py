from djongo import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    age = models.IntegerField()