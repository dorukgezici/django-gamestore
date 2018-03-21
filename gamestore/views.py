from django.shortcuts import render

from django.http import HttpResponse

def dummy_view(request):
    return HttpResponse("This is the dummy Heroku deployment for group g-056 (Django Reinhardt).", content_type="text/plain")