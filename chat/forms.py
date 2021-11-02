from django import forms
from .models import Message, Person

class NewUserForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = Person
        fields = ['username', 'password', 'email']

class ChatUserForm(forms.ModelForm):
    username = forms.CharField()

    class Meta:
        model = Person
        fields = ['username']

class MessageForm(forms.ModelForm):
    message = forms.CharField()

    class Meta:
        model = Message
        fields = ['message']