# Generated by Django 4.0.5 on 2022-06-05 05:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incident_actor',
            options={'verbose_name': 'Incident Actor', 'verbose_name_plural': 'Incident Actors'},
        ),
        migrations.RemoveField(
            model_name='incident',
            name='date',
        ),
        migrations.AddField(
            model_name='incident',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
