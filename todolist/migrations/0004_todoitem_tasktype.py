# Generated by Django 5.0.7 on 2024-08-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_remove_todoitem_priority_todoitem_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='taskType',
            field=models.CharField(choices=[('todo', 'To Do'), ('doToday', 'Do today'), ('inProgress', 'In progress'), ('done', 'Done')], default='todo', max_length=10),
        ),
    ]
