# Generated by Django 5.1.4 on 2024-12-24 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_choicetwo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChoiceTwo',
        ),
    ]