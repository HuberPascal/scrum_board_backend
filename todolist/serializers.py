
from rest_framework import serializers
from todolist.models import  TodoItem
from users.models import CustomUser
from users.serializers import UserSerializer

class TodoItemSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    member_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=CustomUser.objects.all(), write_only=True, source='members'
    )
    class Meta:
        model = TodoItem
        fields = '__all__'
        
    def create(self, validated_data):
        members_data = validated_data.pop('members', [])
        todo_item = TodoItem.objects.create(**validated_data)
        todo_item.members.set(members_data)
        return todo_item

    def update(self, instance, validated_data):
        members_data = validated_data.pop('members', None)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.taskType = validated_data.get('taskType', instance.taskType)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.save()
        
        if members_data is not None:
            instance.members.set(members_data)
        return instance