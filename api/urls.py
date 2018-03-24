from django.urls import path
from .views import save_gamescore, save_gamestate, load_gamestate, set_settings

urlpatterns = [
    path('score', save_gamescore),
    path('save', save_gamestate),
    path('load', load_gamestate),
    path('setting', set_settings)
]
