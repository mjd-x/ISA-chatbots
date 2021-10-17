from django import forms
from .models import User, Message

class UserForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = User
        fields = ['name']

class MessageForm(forms.ModelForm):
    message = forms.CharField()

    class Meta:
        model = Message
        fields = ['message']