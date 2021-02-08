from chat.managers import ThreadManager
from django.db import models





class Message(models.Model):
    thread = models.CharField(max_length=50)
    sender = models.CharField( max_length=50)
    text = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return f'From <Thread - {self.thread}>'
