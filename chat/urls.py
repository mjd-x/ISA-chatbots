from django.urls import path, include

from . import views
from chat.api.views import *

from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="ISA chatbots API",
      default_version='v0.1',
      description="TP ISA 2021 Donis",
      terms_of_service="",
      contact=openapi.Contact(email="mdonis@fie.undef.edu.ar"),
      license=openapi.License(name="-"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


app_name = 'chat'
urlpatterns = [
    path('chat/', views.indexView, name='chat'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('start-chat/', views.formView.as_view(), name='form'),
    path('', views.Login.as_view(), name='login'),
    path('api/start-chat', StartChatView.as_view(), name='start-chat'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('chat.api.router')),
]