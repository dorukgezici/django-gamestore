from django.shortcuts import render
from django.views import generic
from .models import Game


class IndexView(generic.ListView):
    model = Game
    template_name = "index.html"


def example_game(request):
    return render(request, "example_game.html")
