from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from user_auth.sample_data import SAMPLE_TASKS, SAMPLE_USERS
from users.models import CustomUser
from users.serializers import UserSerializer
from todolist.models import  TodoItem
from rest_framework.permissions import AllowAny


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'first_name': user.first_name
        })

class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            
            # Beispiel-Tasks erstellen
            self.create_sample_tasks(user)
            self.create_sample_users(user)
            
            return Response({
                'message': 'User registered successfully',
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'first_name': user.first_name
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_sample_tasks(self, user):
        for task_data in SAMPLE_TASKS:
            TodoItem.objects.create(author=user, **task_data)


    def create_sample_users(self, user):
        for user_data in SAMPLE_USERS:
            if not CustomUser.objects.filter(username=user_data['username']).exists():
                sample_user = CustomUser(
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    username=user_data['username'],
                    email=user_data['email']
                )
                sample_user.set_password("defaultpassword")
                sample_user.save()


