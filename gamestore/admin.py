from django.contrib import admin
from gamestore.models import Developer, Game, GameState, GameOptions, Score, Payment


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(GameState)
class GameStateAdmin(admin.ModelAdmin):
    pass


@admin.register(GameOptions)
class GameOptionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
