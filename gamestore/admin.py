from django.contrib import admin
from tags_input import admin as tags_input_admin
from gamestore.models import Developer, Game, GameState, Score, Payment, Tag


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(tags_input_admin.TagsInputAdmin):
	pass


@admin.register(Game)
class GameAdmin(tags_input_admin.TagsInputAdmin):
    list_display = ('name',)
    #tag_fields = ('tags',)

@admin.register(GameState)
class GameStateAdmin(admin.ModelAdmin):
    pass


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass