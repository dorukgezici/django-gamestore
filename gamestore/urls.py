from django.urls import path
from .views import IndexView, RegistrationView, GameView, GameCreateView, PayView, example_game

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('signup', RegistrationView.as_view(), name="signup"),
    path('game/<int:pk>', GameView.as_view(), name="game"),
    path('game/add', GameCreateView.as_view(), name="game_create"),
    path('pay', PayView.as_view(), name="pay"),
    path('example_game', example_game, name="example_game")
]
