# todolist/models.py
import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    TAG_CHOICES = [
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('green', 'Green'),
    ]
    tags = models.CharField(max_length=6, choices=TAG_CHOICES, default='medium')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f'({self.id}) {self.title}'

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
