# Generated by Django 2.0.3 on 2018-04-12 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0004_auto_20180412_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
