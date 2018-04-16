from django.contrib import admin
from gamestore.models import Developer, Game, GameState, Score, Payment, Tag
#from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from gamestore.forms import CreateGameForm


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(AjaxSelectAdmin):
    form = CreateGameForm


@admin.register(GameState)
class GameStateAdmin(admin.ModelAdmin):
    pass


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
