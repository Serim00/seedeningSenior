# Generated by Django 4.1.4 on 2023-01-16 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loveMessage', '0004_board_delete_lovemessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='writer',
        ),
    ]
