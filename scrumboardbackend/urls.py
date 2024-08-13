from django.contrib import admin
from django.urls import  path

from todolist.views import TodoItemDetailView, UserLoginView, TodoItemAPIView, UserRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegisterView.as_view(), name='register_user'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('todos/', TodoItemAPIView.as_view(), name='todo_items'),
    path('todos/<int:id>/', TodoItemDetailView.as_view(), name='todo_detail'),
]
