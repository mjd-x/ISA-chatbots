from rest_framework import serializers
from ..models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_active', 'last_login']

        abstract = True

    def validate_password(self, value):
        """Hasheo de contraseña"""
        value = make_password(value)

        return value

class PersonSerializer(UserSerializer):
    class Meta:
        model = Person
        exclude = ['is_active', 'last_login', 'is_staff']

class BotSerializer(UserSerializer):
    class Meta:
        model = Bot
        exclude = ['is_active', 'last_login', 'password', 'email', 'is_staff']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'