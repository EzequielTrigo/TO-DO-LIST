# Generated by Django 5.1.4 on 2024-12-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo_task',
            name='task_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo_task',
            name='task_finished_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
    ]