from django.urls import path
from .views import IndexView, RegistrationView, GameView, GameCreateView, PayView, TagCreateView, StatsView, GameUpdateView, payment_view, example_game

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('signup', RegistrationView.as_view(), name="signup"),
    path('game/<int:pk>', GameView.as_view(), name="game"),
    path('game/add', GameCreateView.as_view(), name="game_create"),
    path('tag/add', TagCreateView.as_view(), name="add_tag"),
    path('dev/stats', StatsView.as_view(), name="dev_stats"),
    path('dev/update/<int:pk>', GameUpdateView.as_view(), name="game_update"),
    path('pay', PayView.as_view(), name="pay"),
    path('payment/success', payment_view, name="payment_success"),
    path('payment/cancel', payment_view, name="payment_cancel"),
    path('payment/error', payment_view, name="payment_error"),
    path('example_game', example_game, name="example_game")
]
