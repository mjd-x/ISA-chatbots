from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'people', PersonViewSet)
router.register(r'bots', BotViewSet)

urlpatterns = router.urls