# Generated by Django 4.1.1 on 2022-09-22 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0002_remove_sport_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='sports',
            field=models.ManyToManyField(to='deportes.sport'),
        ),
    ]
