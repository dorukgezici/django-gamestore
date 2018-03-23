from django.urls import path
from .views import save_gamescore, save_gamestate, request_gamestate, load_gamestate, throw_error, set_settings

urlpatterns = [
    path('score', save_gamescore),
    path('save', save_gamestate),
    path('load_request', request_gamestate),
    path('load', load_gamestate),
    path('error', throw_error),
    path('setting', set_settings)
]
