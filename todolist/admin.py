from django.contrib import admin

from todolist.models import CustomUser, TodoItem

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(CustomUser)
