from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.contrib.auth.decorators import login_required
from gamestore.models import Score, Game, GameState, User
from simple_email_confirmation.models import EmailAddress
import json


# REST API

def check_token(token):
    try:
        email = EmailAddress.objects.get(key=token)
        return email.user
    except EmailAddress.DoesNotExist:
        return False


def get_games(request):
    if request.method == "GET":
        try:
            token = request.GET["token"]
            user = check_token(token)
            if not user:
                raise KeyError
            games = Game.objects.all()
            data = serializers.serialize("json", games)
            return JsonResponse(data, safe=False)
        except KeyError:
            return HttpResponseForbidden("Token not accepted.")


def get_leaderboard(request, game_id):
    if request.method == "GET":
        try:
            token = request.GET["token"]
            user = check_token(token)
            if not user:
                raise KeyError
            scores = Score.objects.filter(game_id=game_id)
            data = serializers.serialize("json", scores)
            return JsonResponse(data, safe=False)
        except KeyError:
            return HttpResponseForbidden("Token not accepted.")


def get_my_games(request):
    if request.method == "GET":
        try:
            token = request.GET["token"]
            user: User = check_token(token)
            if not user:
                raise KeyError
            elif not user.is_developer:
                raise PermissionError
            games = Game.objects.filter(developer=user)
            data = serializers.serialize("json", games)
            return JsonResponse(data, safe=False)
        except KeyError:
            return HttpResponseForbidden("Token not accepted.")
        except PermissionError:
            return HttpResponseForbidden("Your account is not a developer account.")


# Game communication

@login_required
def save_gamescore(request):
    data = {"operation": "SCORE"}
    if request.method == "POST":
        game_id = request.POST["gameId"]
        game = Game.objects.get(id=game_id)
        value = request.POST["score"]
        Score.objects.create(
            user=request.user,
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
        game_id = request.POST["gameId"]
        game = Game.objects.get(id=game_id)
        GameState.objects.create(
            user=request.user,
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
        game_id = request.POST["gameId"]
        game = Game.objects.get(id=game_id)
        try:
            game_state = GameState.objects.filter(user=request.user, game=game).first()
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
