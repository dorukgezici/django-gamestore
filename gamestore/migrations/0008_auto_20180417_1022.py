# Generated by Django 2.0.2 on 2018-04-17 07:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0007_auto_20180415_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='cover',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='cover'),
        ),
    ]