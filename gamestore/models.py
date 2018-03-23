from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField()


class Score(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    value = models.ForeignKey(Game, on_delete=models.CASCADE)
