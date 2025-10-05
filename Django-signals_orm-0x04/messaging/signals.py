from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from chats.models import User
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def notify_on_new_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user = instance.receiver,
            message = instance
        )
        print(f"Notification created for {instance.receiver.first_name} about message {instance.id}")

@receiver(pre_save, sender=Message)
def log_message_on_edit(sender, instance, **kwargs):
    """
    Logs the old content of a message
    into a separate MessageHistory model before it’s updated.
    """
    
    if instance.pk:  # check if message already exists and not a new creation
        try:
            old_message = Message.objects.get(pk=instance.pk)
        except Message.DoesNotExist:
            return # message is new, do noting

        # Log if message content change
        if old_message.content != instance.content:
            MessageHistory.objects.create(
                message = old_message,
                old_message = old_message.content
            )
            # Mark as edited
            instance.edited = True

@receiver(post_delete, sender=User)
def delete_related_user_data(sender, instance, **kwargs):
    """
    Ensures all related objects are deleted when a user is removed.
    CASCADE handles most of this, but we can use this hook for extra cleanup.
    """
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    Notification.objects.filter(user=instance).delete()
    
    MessageHistory.objects.filter(message__sender=instance).delete()
