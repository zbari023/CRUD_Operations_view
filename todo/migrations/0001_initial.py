# Generated by Django 4.2.6 on 2023-10-27 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('flag', models.CharField(choices=[('notstarted', 'notstarted'), ('inprogress', 'inprogress'), ('completed', 'completed')], max_length=20)),
                ('created_datum', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
