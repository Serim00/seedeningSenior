# Generated by Django 4.1.4 on 2023-01-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveMessage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('content', models.TextField()),
                ('writer', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
