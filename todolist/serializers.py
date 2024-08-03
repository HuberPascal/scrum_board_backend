
from rest_framework import serializers
from todolist.models import CustomUser, TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
      class Meta:
          model = TodoItem
          fields = '__all__'
          
          
          
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user