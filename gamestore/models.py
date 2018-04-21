from cloudinary import models as cloudinary_models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Game(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField()
    cover = cloudinary_models.CloudinaryField("cover", blank=True)
    price = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Tags")
    created = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            # If the object is created, its creation date is set
            self.created = timezone.now()
        return super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Score(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    value = models.FloatField()

    class Meta:
        ordering = ['-value']

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}$ - {} : {}".format(self.amount, self.game, self.date.strftime("%Y-%m-%d | %H:%m"))
