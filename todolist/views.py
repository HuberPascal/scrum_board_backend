
from rest_framework.response import Response

from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from todolist.models import TodoItem
from todolist.serializers import TodoItemSerializer, UserSerializer
# from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class TodoItemView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        todos = TodoItem.objects.all()
        serializer = TodoItemSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, format=None):
        todo = TodoItem.objects.get(pk=request.data.get('id'))
        serializer = TodoItemSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Todo updated succesfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, format=None):
         todo = TodoItem.objects.get(pk=request.data.get('id'))
         serializer = TodoItemSerializer(todo, data=request.data, partial=True)
         if serializer.is_valid():
             serializer.save()
             return Response({'msg': 'Todo updated succesfully', 'data':serializer.data}, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    def delete(self, request, format=None):
        todo = TodoItem.objects.get(pk=request.data.get('id'))
        todo.delete()
        return Response({'msg': 'Todo deleted successfully'}, status=status.HTTP_200_OK)

        

class LoginView(ObtainAuthToken):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
        
        
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)