def get_threaded_replies(message):
    """
    Recursively build a threaded representation of replies.
    """
    return [
        {
            'id': reply.id,
            'sender': reply.sender.email,
            'content': reply.content,
            'sent_at': reply.sent_at,
            'replies': get_threaded_replies(reply)
        }
        for reply in message.replies.all()
    ]
