from django.urls import path

from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('user/<int:pk>', views.UserView.as_view(), name='user'),
    path('conversacion/<int:pk>', views.ConversacionView.as_view(), name='conversacion'),
    path('mensaje/<int:pk>', views.MensajeView.as_view(), name='mensaje'),
]