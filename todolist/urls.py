from django.urls import path
from .views import TodoItemDetailView, TodoItemAPIView

urlpatterns = [
    path('', TodoItemAPIView.as_view(), name='todo_items'),
    path('<int:id>/', TodoItemDetailView.as_view(), name='todo_detail'),
]