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

    def retrieve(self, request, *args, **kwargs):
        # funcion retrieve comun
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # busco los mensajes en esta conversacion
        message_queryset = Message.objects.filter(idChat=instance.id)

        # funcion list para serializar los mensajes

        # esto se usa cuando son muchos mensajes??
        # page = self.paginate_queryset(message_queryset)
        # if page is not None:
        #     message_serializer = MessageSerializer(page, many=True)
        #     print(f"page: {self.get_paginated_response(message_serializer.data)}")

        # serializo los mensajes de la conversacion
        message_serializer = MessageSerializer(message_queryset, many=True)

        # tomo la data serializada de la conversacion, y le agrego adentro los mensajes
        final_data = serializer.data
        final_data['messages'] = message_serializer.data

        # devolver el dict completo
        return Response(final_data)

