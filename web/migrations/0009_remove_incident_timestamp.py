# Generated by Django 4.0.5 on 2022-06-06 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_incident_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='timestamp',
        ),
    ]
