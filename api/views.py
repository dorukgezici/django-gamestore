from django.http import JsonResponse
from gamestore.models import Score, GameState


def save_gamescore(request):
    json = {}
    if request.method == "POST":
        player = request.user
        game = request.POST["game"]
        value = request.POST["score"]
        Score.objects.create(player, game, value)
        json["success"] = True
    else:
        json["success"] = False
    return JsonResponse(json)


def save_gamestate(request):
    json = {}
    if request.method == "POST":
        game_state = request.POST["gameState"]
        player = request.user
        game = request.POST["game"]
        score = game_state["score"]
        GameState.objects.create(player, game, score)
        json["success"] = True
    else:
        json["success"] = False
    return JsonResponse(json)


def load_gamestate(request, game):
    if request.method == "GET":
        try:
            game_state = GameState.objects.get(player=request.user, game=game).last()
            json = {
                "messageType": "LOAD",
                "gameState": {
                    "score": game_state.score
                }
            }
        except GameState.DoesNotExist:
            json = {
                "messageType": "ERROR",
                "info": "Gamestate could not be loaded."
            }
        return JsonResponse(json)


def set_settings(request):
    json = {}
    return JsonResponse(json)
