from django.http import JsonResponse


def save_gamescore(request):
    json = {
        "messageType": "SCORE"
    }
    return JsonResponse(json)


def save_gamestate(request):
    json = {}
    return JsonResponse(json)


def request_gamestate(request):
    json = {}
    return JsonResponse(json)


def load_gamestate(request):
    json = {}
    return JsonResponse(json)


def throw_error(request):
    json = {}
    return JsonResponse(json)


def set_settings(request):
    json = {}
    return JsonResponse(json)
