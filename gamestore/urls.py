from django.urls import path
from .views import IndexView, RegistrationView, ProfileView, GameView, GameCreateView, TagCreateView, GameUpdateView, delete_game, payment_view, example_game, switch_to_developer, confirm_email

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('signup', RegistrationView.as_view(), name="signup"),
    path('activate/<str:key>', confirm_email, name="confirm_email"),
    path('profile/<int:pk>', ProfileView.as_view(), name="profile"),
    path('profile/switch-to-developer', switch_to_developer, name="switch_to_developer"),
    path('game/<int:pk>', GameView.as_view(), name="game"),
    path('game/add', GameCreateView.as_view(), name="game_create"),
    path('game/update/<int:pk>', GameUpdateView.as_view(), name="game_update"),
    path('game/delete/<int:pk>', delete_game, name="game_delete"),
    path('tag/add', TagCreateView.as_view(), name="add_tag"),
    path('payment/success', payment_view, name="payment_success"),
    path('payment/cancel', payment_view, name="payment_cancel"),
    path('payment/error', payment_view, name="payment_error"),
    path('example_game', example_game, name="example_game")
]
