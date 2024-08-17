
from rest_framework import serializers
from todolist.models import TodoItem

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = [ 'first_name', 'last_name', 'username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = CustomUser(
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             username=validated_data['username'],
#             email=validated_data['email']
#         )
#         user.set_password(validated_data['password'])  # Verschlüsselung des Passworts
#         user.save()
#         return user

# TodoItemSerializer: Serializer für das TodoItem-Modell
class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'