from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.views import  APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from todolist.models import  TodoItem
from todolist.serializers import TodoItemSerializer

class TodoItemAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # Ursprünglich: todos = TodoItem.objects.all()  (nicht löschen)
        # Jetzt: Filtere nur die Aufgaben des aktuell angemeldeten Benutzers
        todos = TodoItem.objects.filter(author=request.user)  # Filter tasks by the logged-in user
        serializer = TodoItemSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoItemDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        todo = get_object_or_404(TodoItem, pk=id)
        serializer = TodoItemSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        todo = get_object_or_404(TodoItem, pk=id)
        serializer = TodoItemSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Todo updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        todo = get_object_or_404(TodoItem, pk=id)
        serializer = TodoItemSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Todo partially updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        todo = get_object_or_404(TodoItem, pk=id)
        todo.delete()
        return Response({'msg': 'Todo deleted successfully'}, status=status.HTTP_200_OK)
    
