from django.urls import path
from .views import IndexView, example_game

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('example_game', example_game, name="example_game")
]
