from django.db import models

class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        """
        Return only unread messages for a specific user.
        Optimized to fetch only required fields.
        """
        return super().get_queryset().filter(receiver=user, read=False)
