# Generated by Django 4.1.1 on 2022-09-22 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='participants',
        ),
    ]
