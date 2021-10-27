from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import *
from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserForm, MessageForm

def indexView(request):
    # messages = Message.objects.all().order_by("date")
    julieBot = User.objects.get(id=1)
    eddieBot = User.objects.get(id=2)

    last_chat = Chat.objects.last()  # encuentra el ultimo chat creado
    messages = Message.objects.filter(idChat=last_chat).order_by("date")

    context = {'messages': messages, 'julieBot': julieBot, 'eddieBot': eddieBot}

    return render(request, 'chat/chat.html', context)


class formView(TemplateView):
    template_name = 'chat/home.html'

    def get(self, request, *args, **kwargs):
        user_form = UserForm()
        message_form = MessageForm()

        return render(request, self.template_name, {'user_form': user_form, 'message_form': message_form})

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)  # llena la form con la data de la POST request
        message_form = MessageForm(request.POST)

        if user_form.is_valid() and message_form.is_valid():  # validacion
            name = user_form.cleaned_data['name']  # seguridad cuando trae la data

            try:
                user = User.objects.get(name=name)  # busco si ya existe el usuario
                # si ya existe ese usuario, lo uso sin guardar de vuelta los datos de la form
            except User.DoesNotExist:  # no existe ese usuario todavia
                user_form.save()  # lo creo
                user = User.objects.get(name=name)  # traigo el usuario que acabo de crear

            message_data = message_form.save(commit=False)  # no guardo en la db todavia
            message = message_form.cleaned_data['message']

            # crear la conversacion
            new_chat = Chat.objects.create(idUser1=user, idUser2=User.objects.get(id=1))  # juliebot

            message_data.idUser = user  # le asigno como sender el usuario
            message_data.idChat = new_chat  # asocio a la conversacion
            message_data.save()  # lo guardo a la db

            print(f"Data: {name}, {message}")
            return redirect('chat:chat')  # redirect a la pagina con el chat

        else:  # algo salio mal, devuelve pagina con los forms limpios
            user_form = UserForm()  # inicializo forms en blanco para "limpiar"
            message_form = MessageForm()

            context = {'user_form': user_form, 'message_form': message_form}
            return render(request, self.template_name, context)
