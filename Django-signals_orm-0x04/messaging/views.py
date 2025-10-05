from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Message
from .utils import get_threaded_replies
from chats.models import User
from chats.serializers import UserSerializer
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from .serializers import MessageSerializer, MessageHistorySerializer

@api_view(['GET'])
@cache_page(60)
def conversation_messages(request, conversation_id):
    messages = Message.objects.filter(conversation_id=conversation_id)\
                               .select_related('sender')\
                               .order_by('sent_at')

    data = [
        {
            "id": msg.id,
            "sender": msg.sender.email,
            "content": msg.content,
            "sent_at": msg.sent_at,
        }
        for msg in messages
    ]
    return Response(data)


class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage Messages and provide access to their edit history
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(detail=True, methods=['get'])
    def history(self, request, pk=None):
        message = self.get_object()
        history = message.edit_history.order_by('-changed_at')
        serializer = MessageHistorySerializer(history, many=True)
        return Response(serializer.data)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['delete'], permission_classes=[permissions.IsAuthenticated])
    def delete_user(self, request):
        """
        Allows the currently authenticated user to delete their account.
        """
        
        user = request.user
        user.delete()
        return Response(
            {"message": "Your account has been deleted."},
            status=status.HTTP_204_NO_CONTENT
        )

class MessageViewSet(viewsets.ViewSet):
    """
    View messages in a threaded format.
    """

    def list(self, request):
        # Get all top-level messages
        messages = Message.objects.filter(parent_message__isnull=True)\
            .select_related('sender')\
            .prefetch_related('replies__sender')

        data = []
        for msg in messages:
            id = msg.id
            sender = request.user
            data.append({
                'id': id,
                'sender': sender,
                'content': msg.content,
                'sent_at': msg.sent_at,
                'replies': get_threaded_replies(msg)
            })

        return Response(data)

class InboxViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # Fetch only unread messages for the logged-in user
        unread_messages = Message.unread.unread_for_user(request.user)\
            .select_related("sender") \
            .only("id", "sender", "content", "created_at")

        data = [
            {
                "id": msg.id,
                "sender": msg.sender,
                "content": msg.content,
                "sent_at": msg.sent_at,
                "read": msg.read,
            }
            for msg in unread_messages
        ]
        return Response(data)
    
    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        try:
            msg = Message.objects.get(pk=pk, receiver=request.user)
            msg.read = True
            msg.save(update_fields=['read'])
            return Response({"message": "Message marked as read"})
        except Message.DoesNotExist:
            return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)

