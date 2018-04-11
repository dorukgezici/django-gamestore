from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from gamestore.models import Payment, Game, Tag

from tags_input import fields, widgets


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = []
        widgets = {
            "player": forms.HiddenInput()
        }

class CreateGameForm(forms.ModelForm):
    tags = fields.TagsInputField( Tag.objects.all(),
                                  create_missing=True,
                                  required=False)
    class Meta:
        model = Game
        fields = ["developer", "name", "url", "cover", "tags"]
        widgets = {
            "tags": widgets.TagsInputWidget
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Your email address')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')
