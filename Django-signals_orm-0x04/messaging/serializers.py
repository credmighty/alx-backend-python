from rest_framework import serializers
from .models import Message, MessageHistory

class MessageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageHistory
        fields = ['id', 'old_content', 'edited_at']

class MessageSerializer(serializers.ModelSerializer):
    edit_history = MessageHistorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'receiver',
            'content',
            'edited',
            'created_at',
            'edit_history',
        ]
