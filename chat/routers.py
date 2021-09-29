from rest_framework.routers import DefaultRouter
from mjd_chatbots.chat.apiviews import UsuarioViewSet

router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet)