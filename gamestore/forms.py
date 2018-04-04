from django import forms
from gamestore.models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = []
        widgets = {
            "player": forms.HiddenInput()
        }
