from django.urls import path
from .views import IndexView, RegistrationView, GameView, GameCreateView, PayView, payment_view, example_game

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('signup', RegistrationView.as_view(), name="signup"),
    path('game/<int:pk>', GameView.as_view(), name="game"),
    path('game/add', GameCreateView.as_view(), name="game_create"),
    path('pay', PayView.as_view(), name="pay"),
    path('payment/success', payment_view, name="payment_success"),
    path('payment/cancel', payment_view, name="payment_cancel"),
    path('payment/error', payment_view, name="payment_error"),
    path('example_game', example_game, name="example_game")
]
