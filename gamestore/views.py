from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from hashlib import md5
from .forms import CustomUserCreationForm, CreateGameForm, SearchForm, CreateTagForm
from .models import User, Game, Score, Payment
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages

# /!\ Development only
# Set to True to test with sqlite
SQLITESAFE = False


class IndexView(generic.ListView):
    model = Game
    template_name = "index.html"
    paginate_by = 12

    def get_queryset(self):
        qs = Game.objects.all()

        try:
            max_price = int(self.request.GET.get("maxprice"))
        except:
            max_price = -1
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

        # page = int(self.request.GET.get("page", "1"))
        # qs = qs[PAGESIZE*(page-1):PAGESIZE*(page-1)+PAGESIZE]
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        objects = context["object_list"]
        for game in objects:
            if not self.request.user.is_authenticated:
                game.possessed = False
            else:
                game.possessed = Payment.objects.filter(user=self.request.user).filter(game=game).exists()

            if SQLITESAFE:
                game.checksum = 0
                continue
            next_payment_id = "{}-{}".format(game.id, get_next_id(Payment))
            game.next_payment_id = next_payment_id
            game.checksum = get_payment_checksum(next_payment_id, game.price)
        context["object_list"] = objects

        form = SearchForm(self.request.GET)
        context["form"] = form

        if context["is_paginated"]:
            page_range = list(context["paginator"].page_range)
            page_number = context["page_obj"].number
            if len(page_range) <= 3:
                context["custom_range"] = page_range
            elif page_number == 1:
                context["custom_range"] = page_range[:3]
            elif context["page_obj"].number == context["paginator"].num_pages:
                context["custom_range"] = page_range[-3:]
            else:
                context["custom_range"] = page_range[page_number-2:page_number+1]
        return context


class GameView(generic.DetailView):
    model = Game
    template_name = "game.html"

    def get(self, request, *args, pk=None, **kwargs):
        if not request.user.is_authenticated:
            possessed = False
        else:
            possessed = Payment.objects.filter(user=request.user).filter(game__id=pk).exists()

        if possessed:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseNotFound("This game doesn't exist or you don't own it.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context["object"]
        scores = Score.objects.filter(game=obj)
        obj.scores = scores
        obj.scores_array = ["#{}: {} by {}".format(i, score.value, score.user) for i, score in enumerate(scores)]
        context["object"] = obj
        context["user"] = self.request.user
        return context


class GameCreateView(generic.FormView):
    form_class = CreateGameForm
    template_name = "game_create.html"
    success_url = "/"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        elif not request.user.is_developer:
            return HttpResponseRedirect(reverse("profile", request.user.id))
        else:
            return super().get(request, *args, **kwargs)

    def get_initial(self):
        return {"developer": self.request.user.id}

    def form_valid(self, form):
        if not self.request.user.is_developer:
            return HttpResponse('Unauthorized', status=401)
        game = form.save()
        Payment.objects.get_or_create(user=self.request.user, game=game, amount=0)
        return super().form_valid(form)


class GameUpdateView(generic.UpdateView):
    model = Game
    form_class = CreateGameForm
    template_name = "game_update.html"
    success_url = "/"

    def get(self, request, *args, pk=None, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        elif Game.objects.get(id=pk).developer != request.user:
            return HttpResponse('Unauthorized', status=401)
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["game"] = self.get_object()
        return context

    def get_initial(self):
        return {"developer": self.request.user.id}

    def form_valid(self, form):
        if self.request.user != self.get_object().developer:
            return HttpResponse('Unauthorized', status=401)
        form.save()
        return super().form_valid(form)


@login_required
def delete_game(request, pk):
    game = Game.objects.get(id=pk)
    if request.user == game.developer:
        game.delete()
    return HttpResponseRedirect("/")


def payment_view(request):
    msg = "Your payment is IN PROCESS!"
    if request.GET.get("result", "error") == "success":
        if "success" in request.path:
            game_id = request.GET["pid"].split("-")[0]
            game = Game.objects.get(id=game_id)
            Payment.objects.create(user=request.user, game=game, amount=game.price)
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
            return HttpResponseRedirect(reverse("login"))
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
        link = reverse("confirm_email", kwargs={"key": user.confirmation_key})
        send_mail("Email Confirmation for Django-Reinhardt", "Welcome to our website!", from_email="Django Reinhardt's Gamestore", recipient_list=[user.email], html_message='<p>Use this link to confirm your email: <a href="http://{}{}">http://{}{}</a></p>'.format(self.request.META['HTTP_HOST'], link, self.request.META['HTTP_HOST'], link))
        if form.cleaned_data["is_developer"]:
            user.is_developer = True
            user.save()
        return super().form_valid(form)


def confirm_email(request, key):
    request.user.confirm_email(key)
    messages.add_message(request, messages.INFO, "Email verified!")
    return HttpResponseRedirect("/")


class ProfileView(generic.DetailView):
    model = User
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        payments = Payment.objects.filter(user=self.request.user)
        context["payments"] = payments
        context["total_spent"] = sum(payment.amount for payment in payments)
        my_games = Game.objects.filter(developer=self.request.user)
        context["my_games"] = my_games
        if self.request.user.is_developer:
            context["developer"] = self.request.user
        else:
            context["developer"] = False
        return context


@login_required
def switch_to_developer(request):
    request.user.is_developer = True
    request.user.save()
    return HttpResponseRedirect(reverse("profile", kwargs={"pk": request.user.id}))
