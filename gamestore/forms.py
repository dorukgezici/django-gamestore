from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from gamestore.models import Payment, Game, Tag
from django.core.validators import MinValueValidator
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
    is_developer = forms.BooleanField(label="Do you want to add your own games as a developer?", required=False)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")


class SearchForm(forms.Form):
    keywords = forms.CharField(label='Keywords', max_length=128, required=False, )
    tags = AutoCompleteSelectMultipleField('tags', label="Tags", help_text="Begin typing to search tags", required=False)
    maxprice = forms.IntegerField(label="Maximum price", validators=[MinValueValidator(0)], required=False)
    sortby = forms.ChoiceField(label="Sort by", choices=[("recent", "Most recent"), ("cheapest", "Cheapest price"), ("alpha", "Alphabetic order")], required=False)
