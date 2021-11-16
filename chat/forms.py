from django import forms
from .models import Message, Person, Bot

class NewUserForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = Person
        fields = ['username', 'password', 'email']

class MessageForm(forms.ModelForm):
    message = forms.CharField()

    class Meta:
        model = Message
        fields = ['message']

class SelectBotForm(forms.Form):
    bot = forms.ModelChoiceField(queryset=Bot.objects.all())