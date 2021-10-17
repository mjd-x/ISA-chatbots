from django.views.generic import TemplateView

from .models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from .forms import UserForm, MessageForm

def indexView(request):
    messages = Message.objects.all().order_by("date")
    julieBot = User.objects.get(id=1)
    eddieBot = User.objects.get(id=2)

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
            user_form.save()
            message_data = message_form.save(commit=False)  # no guardo en la db todavia

            name = user_form.cleaned_data['name']  # seguridad cuando trae la data
            message = message_form.cleaned_data['message']

            user = get_object_or_404(User, name=name)  # busco el usuario que acabo de crear
            message_data.idUser = user  # le asigno como sender el usuario
            message_data.save()  # lo guardo a la db

            print(f"Data: {name}, {message}")

            user_form = UserForm()  # inicializo forms en blanco para "limpiar"
            message_form = MessageForm()
            return redirect('chat:chat')  # redirect a la pagina con el chat

        context = {'user_form': user_form, 'message_form': message_form, 'name': name, 'message': message}
        return render(request, self.template_name, context)

# class IndexView(generic.ListView):
#     template_name = 'chat/chat.html'
#     # context_object_name = 'users_by_name'

#     def get_queryset(self):
#         return User.objects.order_by('nombre')[:10]

# class UserView(generic.DetailView):
#     # user = get_object_or_404(User, pk=user_id)
#     #
#     # return render(request, 'chat/user.html', {'user' : user})
#     model = User
#     template_name = 'chat/user.html'
#
# class ConversacionView(generic.DetailView):
#     model = Conversacion
#     template_name = 'chat/conversacion.html'
#
# class MensajeView(generic.DetailView):
#     model = Mensaje
#     template_name = 'chat/mensaje.html'