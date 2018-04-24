from django.urls import path
from .views import get_games, get_leaderboard, get_my_games, save_gamescore, save_gamestate, load_gamestate

urlpatterns = [
    path('games', get_games, name="games"),
    path('leaderboard/<int:game_id>', get_leaderboard, name="leaderboard"),
    path('my_games', get_my_games, name="my_games"),
    path('score', save_gamescore, name="save_gamescore"),
    path('save', save_gamestate, name="save_gamestate"),
    path('load', load_gamestate, name="load_gamestate")
]
