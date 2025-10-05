from django.test import TestCase
from chats.models import User
from .models import Message, Notification

class MessageSignalTest(TestCase):
    def setUp(self):
        """
        Create test users
        """
        self.sender = User.objects.create_user(
            username='betty',
            email='betty@example.com',
            password='test123',
            first_name='Betty',
            last_name='Smith'
        )
        
        self.receiver = User.objects.create_user(
            username='barry',
            email='barry@example.com',
            password='test123',
            first_name='Barry',
            last_name='Tailor'
        )
    
    def test_notification_created_on_new_message(self):
        # Determine number of notifications if any.
        notification_count = Notification.objects.count()
        
        self.assertEqual(Notification.objects.count(), notification_count)
        
        # Create a new message to trigger the signal
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content="Hello Barry!"
        )
        
        # Confirm an increase in notification count
        self.assertEqual(Notification.objects.count(), notification_count + 1)
        
        # Check that the notification is linked to the correct user and message
        notification = Notification.objects.first()
        self.assertEqual(notification.user, self.receiver)
        self.assertEqual(notification.message, message)
        
