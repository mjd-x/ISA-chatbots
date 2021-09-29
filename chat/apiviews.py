from rest_framework import viewsets
from mjd_chatbots.chat.serializers import *

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects