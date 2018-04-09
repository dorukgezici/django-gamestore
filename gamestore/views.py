from django.shortcuts import render
from django.views import generic
from hashlib import md5
import random
from .forms import PaymentForm
from .models import Game, Score


class IndexView(generic.ListView):
    model = Game
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objects = self.object_list
        for obj in objects:
            scores = Score.objects.filter(game=obj)
            obj.scores = scores
        context["object_list"] = objects
        return context


class GameView(generic.DetailView):
    model = Game
    template_name = "game.html"


class PayView(generic.CreateView):
    form_class = PaymentForm
    template_name = "pay.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


def pay(request):
    url = "https://simplepayments.herokuapp.com/pay/"
    pid = random.randint()
    sid = "g056"
    amount = 0
    secret_key = "0b44e27c9d07c9152f5ffe0604eabfe8"
    checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
    m = md5(checksumstr.encode("ascii"))
    checksum = m.hexdigest()


def example_game(request):
    return render(request, "example_game.html")
