from .models import *
from django.shortcuts import get_object_or_404, render
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'chat/index.html'
    context_object_name = 'users_by_name'

    def get_queryset(self):
        return User.objects.order_by('nombre')[:10]

class UserView(generic.DetailView):
    # user = get_object_or_404(User, pk=user_id)
    #
    # return render(request, 'chat/user.html', {'user' : user})
    model = User
    template_name = 'chat/user.html'

class ConversacionView(generic.DetailView):
    model = Conversacion
    template_name = 'chat/conversacion.html'

class MensajeView(generic.DetailView):
    model = Mensaje
    template_name = 'chat/mensaje.html'

    def addMensaje(request):
        pass