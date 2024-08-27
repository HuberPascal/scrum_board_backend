
from rest_framework import serializers
from contacts.models import Contact
from contacts.serializers import ContactSerializer
from todolist.models import  TodoItem



class TodoItemSerializer(serializers.ModelSerializer):
    author = ContactSerializer(read_only=True)
    members = ContactSerializer(many=True, read_only=True) 
    member_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Contact.objects.all(), write_only=True, source='members'
    )
    class Meta:
        model = TodoItem
        fields = '__all__'
        
    def create(self, validated_data):
        members_data = validated_data.pop('members', [])
        todo_item = TodoItem.objects.create(**validated_data)
        
        # todo_item.members.set(members_data)
        # if todo_item.author in members_data:
        #     members_data.remove(todo_item.author)
    
        #     todo_item.members.set(members_data)
        
        if members_data:
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
            if instance.author in members_data:
                members_data.remove(instance.author)
            instance.members.set(members_data)
        return instance