from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from gamestore.models import Score, Game, GameState
import json


@login_required
def save_gamescore(request):
    data = {"operation": "SCORE"}
    if request.method == "POST":
        player = request.user
        game_id = request.POST["gameId"]
        game = Game.objects.get(id=game_id)
        value = request.POST["score"]
        Score.objects.create(
            player=player,
            game=game,
            value=value
        )
        data["success"] = True
    else:
        data["success"] = False
    return JsonResponse(data)


@login_required
def save_gamestate(request):
    data = {"operation": "SAVE"}
    if request.method == "POST":
        player = request.user
        game_id = request.POST["gameId"]
        game = Game.objects.get(id=game_id)
        GameState.objects.create(
            player=player,
            game=game,
            data=request.POST["gameState"]
        )
        data["success"] = True
    else:
        data["success"] = False
    return JsonResponse(data)


@login_required
def load_gamestate(request):
    if request.method == "POST":
        player = request.user
        game_id = request.POST["gameId"]
        game = Game.objects.get(id=game_id)
        try:
            game_state = GameState.objects.filter(player=player, game=game).first()
            if not game_state:
                raise GameState.DoesNotExist
            data = {
                "messageType": "LOAD",
                "gameState": json.loads(game_state.data)
            }
        except GameState.DoesNotExist:
            data = {
                "messageType": "ERROR",
                "info": "Gamestate could not be loaded."
            }
        return JsonResponse(data)
