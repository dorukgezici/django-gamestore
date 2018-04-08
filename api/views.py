from django.http import JsonResponse
from gamestore.models import Score, Game, GameState, Item


def save_gamescore(request):
    json = {"operation": "SCORE"}
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
        json["success"] = True
    else:
        json["success"] = False
    return JsonResponse(json)


def save_gamestate(request):
    json = {"operation": "SAVE"}
    if request.method == "POST":
        player = request.user
        game_id = request.POST["gameId"]
        game = Game.objects.get(id=game_id)
        score = request.POST["gameState[score]"]
        player_items = request.POST.get("gameState[playerItems]", [])
        obj = GameState.objects.create(
            player=player,
            game=game,
            score=score
        )
        for item in player_items:
            item_obj = Item.objects.get_or_create(name=item, game_state=obj)
            obj.item_set.add(item_obj)
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
