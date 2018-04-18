from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from hashlib import md5
from .forms import PaymentForm, CustomUserCreationForm, CreateGameForm, SearchForm, CreateTagForm
from .models import Game, Score, Payment, Tag
from django.db import connection
from ajax_select.fields import autoselect_fields_check_can_add

# /!\ Development only
# Set to True to test with sqlite
SQLITESAFE = False


class IndexView(generic.ListView):
    model = Game
    template_name = "index.html"

    def get_queryset(self):
        qs = Game.objects.all()

        max_price = int(self.request.GET.get("maxprice", "-1"))
        if max_price >= 0:
            qs = qs.filter(price__lte=max_price)

        keywords = self.request.GET.get("keywords", "").split(" ")
        for word in keywords:
            qs = qs.filter(name__icontains=word)

        tags = self.request.GET.get("tags", "")
        if len(tags) > 2:
            try:
                tags_id = list(map(int, tags[1:-1].split("|")))
                qs = qs.filter(tags__in=tags_id)
            except:
                pass

        qs = qs.distinct()

        sortby = self.request.GET.get("sortby", "recent")
        if sortby == "recent":
            qs = qs.order_by("-created", "name")
        elif sortby == "cheapest":
            qs = qs.order_by("price", "name")
        else:
            qs = qs.order_by("name")

        return qs


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        objects = context["object_list"]
        for game in objects:
            if SQLITESAFE:
                game.checksum = 0
                continue
            next_payment_id = "{}-{}".format(game.id, get_next_id(Payment))
            game.next_payment_id = next_payment_id
            game.checksum = get_payment_checksum(next_payment_id, game.price)
        context["object_list"] = objects

        form = SearchForm(self.request.GET)
        context["form"] = form

        return context


class GameView(generic.DetailView):
    model = Game
    template_name = "game.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context["object"]
        scores = Score.objects.filter(game=obj)
        obj.scores = scores
        obj.scores_array = ["#{}: {} by {}".format(i, score.value, score.player) for i, score in enumerate(scores)]
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
            # post_data["pid"]
            kwargs["data"] = post_data
        return kwargs

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


def payment_view(request):
    if request.GET.get("result", "error") == "success":
        if "success" in request.path:
            game_id = request.GET["pid"].split("-")[0]
            game = Game.objects.get(id=game_id)
            Payment.objects.create(player=request.user, game=game, amount=game.price)
            msg = "Your payment was a SUCCESS!"
    elif "cancel" in request.path:
        msg = "Your payment was CANCELED!"
    elif "error" in request.path:
        msg = "Your payment had an ERROR!"
    return render(request, "payment.html", {"msg": msg})


def get_payment_checksum(pid, amount):
    sid = "g056"
    secret_key = "0b44e27c9d07c9152f5ffe0604eabfe8"
    checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
    m = md5(checksumstr.encode("ascii"))
    checksum = m.hexdigest()
    return checksum


def get_next_id(model_class):
    cursor = connection.cursor()
    cursor.execute("select nextval('{}_id_seq')".format(model_class._meta.db_table))
    row = cursor.fetchone()
    cursor.close()
    return row[0]


def example_game(request):
    return render(request, "example_game.html")


class TagCreateView(generic.FormView):
    form_class = CreateTagForm
    template_name = "tag_create.html"
    success_url = "/tag/add"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/accounts/login")
        else:
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RegistrationView(generic.FormView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
        login(self.request, user)
        return super().form_valid(form)