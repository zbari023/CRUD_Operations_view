# Generated by Django 4.2.6 on 2023-10-27 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='flag',
            new_name='status',
        ),
    ]