from django.urls import path
from .views import IndexView, GameView, PayView, example_game

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('game/<int:pk>', GameView.as_view(), name="game"),
    path('pay', PayView.as_view(), name="pay"),
    path('example_game', example_game, name="example_game")
]
