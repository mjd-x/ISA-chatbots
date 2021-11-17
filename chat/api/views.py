from .serializers import *
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from chat.forms import *
from ..chatbots import *

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = PersonSerializer.Meta.model.objects

class BotViewSet(viewsets.ModelViewSet):
    serializer_class = BotSerializer
    queryset = BotSerializer.Meta.model.objects

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


class StartChatView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name', '')
        message = request.data.get('message', '')
        print(request.data)
        print(f"{name}, {message}")

        # busco o creo el usuario
        try:
            user = User.objects.get(username=name)  # busco si ya existe el usuario
            # si ya existe ese usuario, lo uso sin guardar de vuelta los datos de la form
        except User.DoesNotExist:  # no existe ese usuario todavia
            User.objects.create(username=name)  # lo creo
            user = User.objects.get(username=name)  # traigo el usuario que acabo de crear

        if user:  # validacion
            # crear la conversacion
            new_chat = Chat.objects.create(idUser1=user, idUser2=User.objects.get(id=1))  # juliebot

            # creo el mensaje
            Message.objects.create(idUser=user, idChat=new_chat, message=message)

            chat(message, new_chat)
            
            # devuelvo el objeto

            return Response({'message': 'Chat created', 'uri': f'http://localhost:8000/api/chats/{new_chat.id}'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
