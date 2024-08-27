from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from contacts.models import Contact
from user_auth.sample_data import SAMPLE_TASKS, SAMPLE_CONTACTS
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
            
            # Den Benutzer als eigenen Kontakt hinzufügen
            Contact.objects.create(
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                user=user
            )
            
            # Beispiel-Tasks erstellen
            self.create_sample_tasks(user)
            self.create_sample_contacts(user)
            
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
            
            
    def create_sample_contacts(self, user):
        for contact_data in SAMPLE_CONTACTS:
            # Erzeugt eine eindeutige E-Mail-Adresse für jeden Benutzer
            unique_email = f"{user.username}_{contact_data['email']}"
            Contact.objects.create(
                first_name=contact_data['first_name'],
                last_name=contact_data['last_name'],
                email=unique_email,
                user=user  # Der Kontakt gehört dem neu registrierten Benutzer
            )
