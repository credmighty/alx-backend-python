from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    #define choices for the role field
    ROLE_CHOICES = (
            ('guest', 'Guest'),
            ('host', 'Host'),
            ('admin', 'Admin'),
        )
    #fields
    user_id = model.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
            db_index=True
        )
    first_name = models.CharField(
            max_length=50,
            null=False,
            #blank=False,
            #verbose_name=_("First Name")
        )
    last_name = models.CharField(
            max_length=50,
            null=False,
            #blank=False,
            #verbose_name=_("Last Name")
        )
    email = models.CharField(
            max_length=255,
            null=False,
            blank=False,
            verbose_name=_("Email Address")
        )
    password_hash = models.CharField(
            max_length=128,
            null=False,
            verbose_name=_("Password Hash")
        )
    phone_number = models.CharField(
            max_length=15,
            null=True,
            blank=True,
            verbose_name=_(Phone Number)
        )
    role = models.CharField(
            max_length=10,
            choices=ROLE_CHOICES,
            null=False,
            default='guest',
            verbose_name=_("Role")
        )
    created_at = models.DateTimeField(
            auto_now_add=True,
            verbose_name=_("Created At")
        )

    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        db_table = 'custom_user'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class Message(models.Model):
    message_id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
            db_index=True
        )
    sender_id = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='sent_messages'
        )
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

     class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
        db_table = 'message'
        ordering = ['sent_at']

    def __str__(self):
        return f"Message from {self.sender_id}: {self.message_body} at {sent_at}"


class Conversation(models.Model):
    converssation_id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
            db_index=True
        )
    participants_id = models.ManyToManyField(
            User,
            related_name='conversations'
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Conversation")
        verbose_name_plural = _("Conversations")
        db_table = 'conversation'

    def __str__(self):
        participant_emails = ', '.join([user.email for user in self.participants_id.all()])
        return f"Conversation {self.conversation_id} ({participant_emails})"
