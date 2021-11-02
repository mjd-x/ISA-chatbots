from django import forms
from .models import User, Message

# password = forms.CharField(widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    username = forms.CharField()

    class Meta:
        model = User
        fields = ['username']

class MessageForm(forms.ModelForm):
    message = forms.CharField()

    class Meta:
        model = Message
        fields = ['message']