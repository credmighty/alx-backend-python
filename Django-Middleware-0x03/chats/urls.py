from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

# Top-level router for conversations
router = DefaultRouter()

router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# Nested router for messages inside conversations
conversation_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversation_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(conversation_router.urls)),
]
