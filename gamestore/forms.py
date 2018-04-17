from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from gamestore.models import Payment, Game, Tag

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
    tags = AutoCompleteSelectMultipleField('tags', required=False, help_text="Begin typing to search tags")

    class Meta:
        model = Game
        fields = ["developer", "name", "url", "cover", "price", "tags"]


class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Your email address")
    is_developer = forms.BooleanField(label="Do you want to add your own games as a developer?")

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")


class SearchForm(forms.Form):
    keywords = forms.CharField(label='Keywords', required=False, max_length=128)
    tags = AutoCompleteSelectMultipleField('tags', required=False, help_text="Begin typing to search tags")