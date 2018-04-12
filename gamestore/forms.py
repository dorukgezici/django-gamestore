from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from gamestore.models import Payment, Game

from ajax_select.fields import AutoCompleteSelectMultipleField


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = []
        widgets = {
            "player": forms.HiddenInput(),
            "game": forms.HiddenInput()
        }


class CreateGameForm(forms.ModelForm):
    tags = AutoCompleteSelectMultipleField('tags', required=False)

    class Meta:
        model = Game
        fields = ["developer", "name", "url", "cover", "tags"]


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Your email address")
    is_developer = forms.BooleanField(label="Do you want to add your own games as a developer?")

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")
