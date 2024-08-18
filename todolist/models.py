# todolist/models.py
import datetime
from django.conf import settings
from django.db import models

from users.models import CustomUser


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    TAG_CHOICES = [
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('red', 'Red'),
        ('orange', 'Orange'),
        ('purple', 'Purple'),
        ('magenta', 'Magenta'),
        ('cyan', 'Cyan'),
    ]
    
    TASK_TYPE_CHOICES = [
        ('todo', 'To-do'),
        ('doToday', 'Do today'),
        ('inProgress', 'In progress'),
        ('done', 'Done'),
    ]
    tags = models.CharField(max_length=7, choices=TAG_CHOICES, default='medium')
    taskType = models.CharField(max_length=10, choices=TASK_TYPE_CHOICES, default='todo')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f'({self.id}) {self.title}'

