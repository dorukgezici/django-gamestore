from django.contrib.auth.models import User
from django.db import models


class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class GameOptions(models.Model):
    width = models.IntegerField(default=800)
    height = models.IntegerField(default=600)

    def __str__(self):
        return "{}x{}".format(self.width, self.height)


class Game(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField()
    options = models.ForeignKey(GameOptions, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Score(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return "{} at {} by {}".format(self.value, self.game, self.player)


class GameState(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return "{} at {} by {}".format(self.score, self.game, self.player)


class Payment(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.player) + ": " + self.amount
