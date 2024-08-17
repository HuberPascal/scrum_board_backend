from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from users.serializers import UserSerializer
from todolist.models import  TodoItem


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            
            # Beispiel-Tasks erstellen
            self.create_sample_tasks(user)
            
            return Response({
                'message': 'User registered successfully',
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_sample_tasks(self, user):
        sample_tasks = [
            {"title": "Welcome to your Kanban board!", "description": "This is your first task", "taskType": "todo", "tags": "blue"},
            {"title": "Add your first real task", "description": "Start managing your tasks", "taskType": "doToday", "tags": "green"},
            {"title": "Drag and drop tasks", "description": "Try dragging tasks between columns", "taskType": "inProgress", "tags": "yellow"},
        ]
        
        for task_data in sample_tasks:
            TodoItem.objects.create(author=user, **task_data)

