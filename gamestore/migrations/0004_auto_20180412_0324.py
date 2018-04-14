# Generated by Django 2.0.3 on 2018-04-12 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0003_auto_20180411_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='tags',
            field=models.ManyToManyField(blank=True, to='gamestore.Tag', verbose_name='Tags'),
        ),
    ]