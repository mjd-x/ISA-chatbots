from .serializers import *
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = MessageSerializer.Meta.model.objects

class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    queryset = ChatSerializer.Meta.model.objects