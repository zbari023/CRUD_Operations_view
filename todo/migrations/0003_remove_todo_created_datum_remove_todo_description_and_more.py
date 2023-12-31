# Generated by Django 4.2.6 on 2023-11-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_flag_todo_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_datum',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
        migrations.AddField(
            model_name='todo',
            name='Action',
            field=models.TextField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='Notes',
            field=models.TextField(default=2, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='todo',
            field=models.TextField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
