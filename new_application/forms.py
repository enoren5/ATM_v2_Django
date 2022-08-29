from django import forms
from .models import User
from django.forms import ModelForm


class BankAccountApplicationForm(ModelForm):
    class  Meta:
        model = User
        fields = ['first_name', 'last_name', 'card_num']