# Generated by Django 2.0.2 on 2018-04-23 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='user',
            new_name='developer',
        ),
    ]
