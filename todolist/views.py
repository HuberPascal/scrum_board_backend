from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from todolist.models import TodoItem
from todolist.serializers import TodoItemSerializer, UserSerializer


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key, # Token wird zurückgegeben
            'user_id': user.pk, # pk = Primary Key
            'email': user.email
        })
    

class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Benutzer wird erstellt
            token, created = Token.objects.get_or_create(user=user)  # Token wird erstellt
            
            
            self.create_sample_tasks(user) # Muster-Tasks erstellen
            
            return Response({
                'message': 'User registered successfully',
                'token': token.key,  # Token wird zurückgegeben
                'user_id': user.pk, # pk = Primary Key
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_sample_tasks(self, user):
        # Liste von Beispiel-Tasks
        sample_tasks = [
            {"title": "Welcome to your Kanban board!", "description": "This is your first task", "taskType": "todo", "tags": "blue"},
            {"title": "Add your first real task", "description": "Start managing your tasks", "taskType": "doToday", "tags": "green"},
            {"title": "Drag and drop tasks", "description": "Try dragging tasks between columns", "taskType": "inProgress", "tags": "yellow"},
        ]
        
        for task_data in sample_tasks:
            TodoItem.objects.create(author=user, **task_data)


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