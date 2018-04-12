from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from hashlib import md5
import random
from .forms import PaymentForm, CustomUserCreationForm, CreateGameForm
from .models import Game, Score, Developer


class IndexView(generic.ListView):
    model = Game
    template_name = "index.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     objects = self.object_list
    #     for obj in objects:
    #         scores = Score.objects.filter(game=obj)
    #         obj.scores = scores
    #     context["object_list"] = objects
    #     return context


class GameView(generic.DetailView):
    model = Game
    template_name = "game.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context["object"]
        scores = Score.objects.filter(game=obj)
        obj.scores = scores
        context["object"] = obj
        return context


class GameCreateView(generic.FormView):
    form_class = CreateGameForm
    template_name = "game_create.html"
    success_url = "/"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/accounts/login")
        else:
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PayView(generic.CreateView):
    form_class = PaymentForm
    template_name = "pay.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "POST":
            post_data = kwargs["data"].copy()
            post_data["sid"] = self.request.user.id
            post_data["pid"]
            kwargs["data"] = post_data
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


class RegistrationView(generic.FormView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
        login(self.request, user)
        return super().form_valid(form)
