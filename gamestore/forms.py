from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from gamestore.models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = []
        widgets = {
            "player": forms.HiddenInput(),
            "game": forms.HiddenInput()
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Your email address')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')
