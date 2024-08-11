# Generated by Django 5.0.7 on 2024-08-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_alter_todoitem_tasktype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='tags',
            field=models.CharField(choices=[('yellow', 'Yellow'), ('blue', 'Blue'), ('green', 'Green'), ('red', 'Red'), ('orange', 'Orange'), ('purple', 'Purple'), ('magenta', 'Magenta'), ('cyan ', 'Cyan')], default='medium', max_length=7),
        ),
    ]
