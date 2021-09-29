from rest_framework import serializers
from mjd_chatbots.chat.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'