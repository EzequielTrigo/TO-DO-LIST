# Generated by Django 5.1.4 on 2024-12-26 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_comments', models.CharField(max_length=20000)),
                ('task_start_date', models.DateTimeField(verbose_name='date published')),
                ('task_expected_finish_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
