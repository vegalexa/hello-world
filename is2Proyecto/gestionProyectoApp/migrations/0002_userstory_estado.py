# Generated by Django 4.1 on 2022-10-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionProyectoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='estado',
            field=models.CharField(default='Por hacer', max_length=200),
        ),
    ]
