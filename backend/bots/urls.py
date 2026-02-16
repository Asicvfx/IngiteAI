from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TelegramBotViewSet, KnowledgeItemViewSet, WebhookView

router = DefaultRouter()
router.register(r'knowledge', KnowledgeItemViewSet, basename='knowledge')
router.register(r'', TelegramBotViewSet, basename='bot')

urlpatterns = [
    path('webhook/<str:token>/', WebhookView.as_view(), name='webhook'),
    path('', include(router.urls)),
]
