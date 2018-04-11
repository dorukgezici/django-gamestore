from django.contrib.auth.models import User
from django.db import models


class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Game(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField()
    cover = models.ImageField(blank=True, null=True, upload_to="covers")
    tags = models.ManyToManyField(Tag, blank=True,
         related_name="games",
         verbose_name='Tags', help_text='Missing items will be auto-created')

    def __str__(self):
        return self.name


class Score(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    value = models.FloatField()

    class Meta:
        ordering = ['value']

    def __str__(self):
        return "{} by {}".format(self.value, self.player)


class GameState(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    data = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "{}: {} by {}".format(self.date, self.game, self.player)


class Payment(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.player) + ": " + self.amount
