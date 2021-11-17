from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import *
from django.shortcuts import render, redirect
from .forms import MessageForm, NewUserForm, SelectBotForm
from .chatbots import *
from django.contrib.auth.mixins import LoginRequiredMixin

#######################
# VIEWS
#######################

@login_required
def chatView(request):
    julieBot = User.objects.get(id=1)
    eddieBot = User.objects.get(id=2)

    # encuentra el ultimo chat creado por la persona
    last_chat = Chat.objects.filter(idUser1=request.user.id).last()
    messages = Message.objects.filter(idChat=last_chat).order_by("date")

    context = {'messages': messages, 'julieBot': julieBot, 'eddieBot': eddieBot}

    return render(request, 'chat/chat.html', context)

class RegisterView(TemplateView):
    template_name = 'chat/create.html'

    def get(self, request, *args, **kwargs):
        user_form = NewUserForm()

        return render(request, self.template_name, {'user_form': user_form})

    def post(self, request, *args, **kwargs):
        user_form = NewUserForm(request.POST)

        if user_form.is_valid():
            user_data = user_form.save(commit=False)
            password = user_form.cleaned_data['password']
            user_data.password = make_password(password)
            user_data.save()

            return redirect('chat:login')
        else:
            user_form = NewUserForm()  # inicializo forms en blanco para "limpiar"

            context = {'user_form': user_form}
            return render(request, self.template_name, context)

class FormView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/start_chat.html'

    def get(self, request, *args, **kwargs):
        bot_form = SelectBotForm()
        message_form = MessageForm()

        return render(request, self.template_name, {'bot_form': bot_form, 'message_form': message_form})

    def post(self, request, *args, **kwargs):
        # llena la form con la data de la POST request
        bot_form = SelectBotForm(request.POST)
        message_form = MessageForm(request.POST)

        if bot_form.is_valid() and message_form.is_valid():  # validacion
            name = request.user.username  # seguridad cuando trae la data

            try:
                user = User.objects.get(username=name)  # busco si ya existe el usuario
                # si ya existe ese usuario, lo uso sin guardar de vuelta los datos de la form
            except User.DoesNotExist:  # no existe ese usuario todavia
                return HttpResponse({"error": "user does not exist"})

            bot_data = bot_form.cleaned_data['bot']
            print(bot_data, bot_data.id)

            message_data = message_form.save(commit=False)  # no guardo en la db todavia
            message = message_form.cleaned_data['message']

            # crear la conversacion
            new_chat = Chat.objects.create(idUser1=user, idUser2=bot_data)  # elegir bot

            message_data.idUser = user  # le asigno como sender el usuario
            message_data.idChat = new_chat  # asocio a la conversacion
            message_data.save()  # lo guardo a la db

            print(f"Data: {name}, {message}")

            chat(message, new_chat)
            return redirect('chat:chat')  # redirect a la pagina con el chat

        else:  # algo salio mal, devuelve pagina con los forms limpios
            # inicializo form en blanco para "limpiar"
            bot_form = SelectBotForm()
            message_form = MessageForm()

            context = {'bot_form': bot_form, 'message_form': message_form}
            return render(request, self.template_name, context)
